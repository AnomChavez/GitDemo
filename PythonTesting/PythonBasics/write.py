#read the file and store all the lines in list
#reverse the list
#write the list back to the file


with open('test.txt', 'r') as reader:
    content = reader.readlines()  #[abc, bdfasdf, cat, dog, elephant]
    reversed(content)  #[elephant, dog, cat, bdfasdf, abc]
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)
