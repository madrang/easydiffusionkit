from setuptools import setup, find_packages
import platform

# hack inspired by https://github.com/pytorch/pytorch/issues/50718#issuecomment-1329360776
def install_torch(package: str, version: str):
    if platform.system() == "Darwin":
        return f'{package}=={version}'

    cuda_version = 'cu116'
    python_version = ''.join(platform.python_version().split('.')[:2])
    os = ''

    include_cuda_in_filename = True
    if platform.system() == "Windows":
        os = 'win_amd64'
    elif platform.system() == "Linux":
        if platform.machine().lower() == 'aarch64':
            os = 'manylinux2014_aarch64'
            include_cuda_in_filename = False
        else:
            os = 'linux_x86_64'

    if include_cuda_in_filename:
        wheel_filename = f'{package}-{version}%2B{cuda_version}-cp{python_version}-cp{python_version}-{os}.whl'
    else:
        wheel_filename = f'{package}-{version}-cp{python_version}-cp{python_version}-{os}.whl'

    return f'{package} @ https://download.pytorch.org/whl/{cuda_version}/{wheel_filename}'

setup(
    name='ldm',
    version='0.0.1',
    description='',
    packages=find_packages(),
    install_requires=[
        install_torch('torch', '1.12.1'),
        install_torch('torchvision', '0.13.1'),

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
