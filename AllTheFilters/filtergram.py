import filters
def main():
    filename = input("Enter the name of the file you want to filter: ")

    img = filters.load_img(filename)
    newImage = filters.obamicon(img)
    filters.save_img(newImage, "recolored.png")

if __name__ == '__main__':
  main()
