from setuptools import setup, find_packages

setup(
    name='stable-diffusion-sdkit',
    version='2.1.0',
    description='',
    packages=find_packages(),
    install_requires=[
        "albumentations==1.3.0",
        "opencv-python==4.6.0.66",
        "pytorch-lightning==1.4.2",
        "omegaconf==2.1.1",
        "test-tube>=0.7.5",
        "einops==0.3.0",
        "transformers==4.19.2",
        "kornia==0.6",
        "open_clip_torch==2.0.2",
        "torchmetrics==0.6.0",
        "tqdm",
    ],
)
