INPUT_SCHEMA = {
    "prompt": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["a black cat with glowing eyes, cute, adorable, disney, pixar, highly detailed, 8k"]
    },
    "img_url": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/diffusers/inpaint.png"]
    },
    "mask_url": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/diffusers/inpaint_mask.png"]
    }
}
