import os
import argparse
import sys
import json
import requests
from datetime import datetime
from dashscope import MultiModalConversation
import dashscope

# Set default base URL
dashscope.base_http_api_url = 'https://dashscope.aliyuncs.com/api/v1'

def generate_image(prompt, output_dir, api_key=None):
    """
    Generates an image using Alibaba Cloud's Qwen-Image-2.0 model based on the prompt.
    """
    if not api_key:
        api_key = os.environ.get("DASHSCOPE_API_KEY")
    
    if not api_key:
        print("Error: DASHSCOPE_API_KEY not found in environment variables or arguments.")
        sys.exit(1)

    # Prepare messages
    # For text-to-image, we just provide the text prompt in the message
    messages = [
        {
            "role": "user",
            "content": [
                {"text": prompt}
            ]
        }
    ]

    try:
        print(f"Generating image using Qwen-Image-2.0 for prompt: {prompt[:50]}...")
        
        response = MultiModalConversation.call(
            api_key=api_key,
            model="qwen-image-2.0",
            messages=messages,
            result_format='message',
            stream=False,
            n=1,
            watermark=False # User might prefer no watermark for production use, but can be toggled
        )
        
        if response.status_code == 200:
            # Parse response to find image URL
            # Structure usually: response.output.choices[0].message.content[0].image
            # Let's inspect the response structure based on common dashscope patterns
            
            try:
                # The response object from dashscope SDK is usually an object, not just dict
                # We can access attributes directly
                content_list = response.output.choices[0].message.content
                image_url = None
                for item in content_list:
                    if 'image' in item:
                        image_url = item['image']
                        break
                
                if not image_url:
                    print("Error: No image URL found in response.")
                    print(json.dumps(response, ensure_ascii=False, default=lambda o: o.__dict__))
                    sys.exit(1)
                    
                # Download the image
                img_data = requests.get(image_url).content
                
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"illustration_qwen_{timestamp}.png"
                output_path = os.path.join(output_dir, filename)
                
                with open(output_path, 'wb') as handler:
                    handler.write(img_data)
                    
                print(f"Image successfully generated and saved to: {output_path}")
                return output_path

            except Exception as e:
                print(f"Error parsing response: {str(e)}")
                print(json.dumps(response, ensure_ascii=False, default=lambda o: o.__dict__))
                sys.exit(1)
        else:
            print(f"Error generating image. Status code: {response.status_code}")
            print(f"Message: {response.message}")
            sys.exit(1)

    except Exception as e:
        print(f"Error generating image: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate an image from a prompt using Qwen-Image-2.0.')
    parser.add_argument('--prompt', type=str, required=True, help='The prompt for the image')
    parser.add_argument('--output-dir', type=str, default='.', help='Directory to save the image')
    parser.add_argument('--api-key', type=str, help='DashScope API Key')

    args = parser.parse_args()
    
    # Ensure output directory exists
    os.makedirs(args.output_dir, exist_ok=True)

    generate_image(args.prompt, args.output_dir, args.api_key)
