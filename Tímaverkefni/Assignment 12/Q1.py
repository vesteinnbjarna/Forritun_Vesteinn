
def music_func(music ='Classic Rock', group = 'The Beatles', singer = 'Freddie Mercury'):
    print('The best type of music is {}'.format(music))
    print ('The best music group is {}'.format(group))
    print('The best lead vocalist is {}'.format(singer))
  




def main():
    try: 
        music, group, singer = input("Input music, group, singer: ").split(',')
        music_func(music, group, singer)
        music_func()
    
    except:
        music_func()
    

main()