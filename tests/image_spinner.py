from image_utils import rotate_image, argparse_arguments
def main():
    image_path, rotate_angle, save_path, force = argparse_arguments()

    rotate_image(
        image_path,
        rotate_angle,
        save_path,
        force
    )
if __name__ == '__main__':
    main()



