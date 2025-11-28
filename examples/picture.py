#!/usr/bin/env python

import base64

from aimlapi import AIMLAPI

# gets AIML_API_KEY from your environment variables
aimlapi = AIMLAPI()

prompt = "An astronaut lounging in a tropical resort in space, pixel art"
model = "dall-e-3"


def example_url():
    print("\n=== Example 1: URL response ===")

    response = aimlapi.images.generate(
        prompt=prompt,
        model=model,
    )

    # Prints response containing a URL link to image
    print(response)


def example_b64():
    print("\n=== Example 2: Base64 response (b64_json) ===")

    response = aimlapi.images.generate(
        prompt=prompt,
        model=model,
        response_format="b64_json",
    )

    print("Raw response:")
    print(response)

    # Decode and save image
    b64 = response.data[0].b64_json
    img_bytes = base64.b64decode(b64)
    with open("generated_image.png", "wb") as f:
        f.write(img_bytes)

    print("Saved generated_image.png")


def main() -> None:
    example_url()
    example_b64()


if __name__ == "__main__":
    main()
