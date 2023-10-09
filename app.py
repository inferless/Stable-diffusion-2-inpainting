import PIL
import requests
import torch
import base64
from io import BytesIO
from diffusers import StableDiffusionInpaintPipeline


class InferlessPythonModel:
    def download_image(url):
        response = requests.get(url)
        return PIL.Image.open(BytesIO(response.content)).convert("RGB")

    def initialize(self):
        self.pipe = StableDiffusionInpaintPipeline.from_pretrained(
            "runwayml/stable-diffusion-inpainting",
            torch_dtype=torch.float16,
        )
        self.pipe = self.pipe.to("cuda:0")

    def infer(self, prompt, image_url, mask_url):
        init_image = InferlessPythonModel.download_image(image_url).resize((512, 512))
        mask_image = InferlessPythonModel.download_image(mask_url).resize((512, 512))
        inpaint_image = self.pipe(
            prompt=prompt, image=init_image, mask_image=mask_image
        ).images[0]
        buff = BytesIO()
        inpaint_image.save(buff, format="PNG")
        img_str = base64.b64encode(buff.getvalue())
        return img_str

    def finalize(self):
        self.pipe = None
