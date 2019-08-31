# https://github.com/pytorch/examples/blob/master/imagenet/main.py
from torchvision import transforms
from .imageh5 import ImageHDF5Dataset

from . import get_data_paths

normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225])
shape = (1, 224, 224)


def train_dataset(preproc=True):

    data_paths = get_data_paths()

    train_preprocessing = None
    if preproc:
        train_preprocessing = transforms.Compose([
            transforms.RandomResizedCrop(224),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            normalize,
        ])

    train_dataset = ImageHDF5Dataset(data_paths['ImageNetHDF5'] / 'ILSVRC2012_img_train.h5',
                                     transform=train_preprocessing)
    return train_dataset


def val_dataset(preproc=True):

    data_paths = get_data_paths()

    val_preprocessing = None
    if preproc:
        val_preprocessing = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            normalize,
        ])

    val_dataset = ImageHDF5Dataset(data_paths['ImageNetHDF5'] / 'ILSVRC2012_img_val.h5',
                                   transform=val_preprocessing)
    return val_dataset
