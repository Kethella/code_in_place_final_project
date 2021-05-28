import os
from PIL import Image
import random
import time

IMAGE_PATH = r'C:\Users\HP\PycharmProjects\code_in_place_final_project\fotos'

def main():
    """
    Put the images inside IMAGE_PATH file in a list
    Introduce the game and ask for user input to start and stop the game
    If user wants to play, start a loop according to the user command for the game
    """
    mimica_game_image_list = create_image_list(IMAGE_PATH)
    print("Welcome to MIMICA GAME!")
    user_input = input("Press enter to start and get character or 0 to leave: ")
    while user_input != "0":
        if user_input == "":
            show_random_image(mimica_game_image_list)
            time.sleep(5)
            user_input = input("Press enter to get character or 0 to leave: ")
        else:
            user_input = input("Press enter to get character or 0 to leave: ")
    print("Thanks for playing! See you next time!")


def show_random_image(image_list):
    """
    Create a random num from 0 to the length of the list (*the last position in the list represent list length - 1)
    After that show the image correspondent to the random number position in the list
    """
    random_num = random.randint(0, (len(image_list)-1))
    random_img = image_list[random_num]
    random_img.show()


def create_image_list(path_to_images):
    """
    Search for the file with images in the computer and add it in a image list
    to have positions (from 0 to ...) to use later with random numbers
    """
    empty_list = []
    for subdirectories, directories, files in os.walk(path_to_images):

        for mimica_game in files:
            file_local = mimica_game
            #printing .png and .jpg files recursively
            if file_local.endswith(".jpg") or file_local.endswith(".png"):
                image = Image.open(str(subdirectories) + "\\" + str(file_local))
                empty_list.append(image)
    full_list = empty_list
    return full_list


if __name__ == '__main__':
    main()
