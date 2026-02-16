from PIL import Image
from pathlib import Path
import argparse
import sys


def main():
    image_path, rotate_angle, save_path = argparse_arguments()

    # Open the image file
    with Image.open(image_path) as img:
        rotater = img.rotate(rotate_angle, expand=True)
        rotater.save(save_path)



def argparse_arguments():

    parser = argparse.ArgumentParser(
        description="Rotate an image",
        epilog=r"Example: python main.py C:OneDrive\Pictures\aaaa.jpg 90 b.jpg or you can use flags or even mix do -h to see them",
        prog="rotate_image"
    )

    parser.add_argument("-i","--image", help="Path to image", type=Path)
    parser.add_argument("-r","--rotate", help="Angle to rotate the image", default= 90 ,type=str)
    parser.add_argument("-s","--save", help="Save image", default="image.jpg",type=str)
    parser.add_argument("--force", action="store_true", help="Allow overwriting the original image")


    parser.add_argument("positional_image", nargs="?", type=Path, help="Image if no flag is used")
    parser.add_argument("positional_rotate", nargs="?", type=int, help="Rotation if no flag is used")
    parser.add_argument("positional_save", nargs="?", type=str, help="Image if no flag is used")

    args = parser.parse_args()

    image_path = Path(args.image or args.positional_image)
    rotate_angle = args.rotate if args.rotate != 90 else (args.positional_rotate or args.rotate)
    save_path = Path(args.save if args.save != "image.jpg" else (args.positional_save or args.save))

    if image_path.resolve() == save_path.resolve() and not args.force:
        print("you are trying to overwrite your image.jpg file, are you sure you want that? use --force to do this")
        sys.exit()

    if not image_path or not image_path.exists():
        parser.error(f"Image file {image_path} does not exist")

    else:
        return image_path, rotate_angle, save_path



if __name__ == "__main__":
    main()

