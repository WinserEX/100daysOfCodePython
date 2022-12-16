print('''
                             /////'
                             '  # o
                             C   - |
                ___          '  =__'        ___
               (` _ \_       |   |        _/  ')
                \  (__\  ,---- _ |----.  /__)- |
                 \__  ( (           /  ) )  __/
                   |_X_\/ \.   #  _.|  \/_X_|
                     |  \ /(   /    /\ /  |
                      \ /  (  ,    /  \ _/
                           /______/
                          [:::::::]
                         /*%*%*%*%*\
                         >%*%#%*%*%|
                        /%*%*#*%*%*\
                       ######^######  b'ger
''')
print("Prepare yourself for the fight of the century!")
print('You will have to fight for survival')

step1 = input("A quick punch is coming your way, which direction would you like to move towards? Type left or right ").lower()
print(step1)

if step1 == "left":
    print("You narrowly evaded a punch that could have blown your head off!!!")
    print('''>
>                             __________________
>               .{{{}}.     .'                  `.
>              {{{}}}}}}   |   COME ON! COME ON!  |
>             {{}}<@ <@}}  |    HIT ME! HIT ME!   |
>             {(     \ )}   \  I DARE YOU TO! ... /
>            {{`|    o(}} --'`._________________.'
>            {{{{\ ____)}
>           {{{{{{|  |}}}}         .--.
>           {{.--'    `--.        /-|  \
>          {{/ \ `.__.' | `.     /\\`..'
>          {/   )       |   \  .' .'""
>          /   /   )__  )    \/  /
>         / .---._.'  \ |`.     /
>        (       H     )|  `._.'
>         `-----' `---' | 
>               |       | 
>               /       \
>              |         |
>              |         |
>              '`-._   .'`.
>             |     \_/    \
>             |      |      \
>             |      |       \
>             |      |\       \
>             |      F `.      \
>             J     J    \      )
>              )    |     )    |
>              /    )     /    |
>              |    |     |    |
>              \    |      \   |          VK
>               \---|       \--|
>               )  x\       )  <`vv-.
>               (_  x`.     (__.____/
>                 `. x )
>                   `-' ''')
    step2 = input("Your opponent is glaring at you, what will you do? Type punch or wait ").lower()
    if step2 == "punch":
        print("You almost knocked him out!!!")

        step3 = input("Your opponent is intimidated, but not beaten yet. What will you do? Type kick, wrestle or punch ").lower()
        if step3 == "punch":
            print("Your opponent was too slow to react, you knocked him out!!! YOU WIN")
            print('''      ,.
                     .---
                     / # o
                     \,__>
                  .o-'-'--._
                 / |\_      '.
                |  |  \   -,  \
                \  /   \__| ) |
                 '|_____[)) |,/
                    |===H=|\ >>
                    \  __,| \_\
                     \/   \  \_\
                     |\    |  \/
                     | \   \   \\
                     |  \   |   \\
                     |__|\ ,-ooD \\
                     |--\_(\.-'   \o
             snd     '-.__) ''')
        elif step3 == "kick":
            print("Your opponent grabbed your leg viciously and broke it, GAME OVER!!!")
            print('''       ___             ___
      //  \           //  \
     //    )         //    )
     ||  _/          ||  _/                   __
     ||  \\_,&__     ||  \\                  (  \
     )|   ^  /  ``---,_\_/ &                 _>  )
     \|___,__\__       `\_  \_              (   /
                \__,-,    `\__\_             >_/
                     \_    /    `\_         / /
                       \_ /        \__    _/ /
                         `\          `\_,/  /
                     _     \__,-,  `   (_  /
                  __( \        ,)__   _/ \/
                 /     `-,___,-'   \_(  O `\
                 \     /_|___   ____/ \  \ =}
                  `---'      `-'       \_=_/{}
                                      .{}{}{}{.
mic                                   {}{}{}{}{
                                      }{}{}{}{}
                                      `}{}{}{}'
                                       `}{}{}''')
        else:
            print("Your opponent is a wresteling expert, GAME OVER!!!")
            print('''       ___             ___
      //  \           //  \
     //    )         //    )
     ||  _/          ||  _/                   __
     ||  \\_,&__     ||  \\                  (  \
     )|   ^  /  ``---,_\_/ &                 _>  )
     \|___,__\__       `\_  \_              (   /
                \__,-,    `\__\_             >_/
                     \_    /    `\_         / /
                       \_ /        \__    _/ /
                         `\          `\_,/  /
                     _     \__,-,  `   (_  /
                  __( \        ,)__   _/ \/
                 /     `-,___,-'   \_(  O `\
                 \     /_|___   ____/ \  \ =}
                  `---'      `-'       \_=_/{}
                                      .{}{}{}{.
mic                                   {}{}{}{}{
                                      }{}{}{}{}
                                      `}{}{}{}'
                                       `}{}{}''')
    else:
        print("You waited for too long, your opponent kicked you so hard that he broke your spine, GAME OVER!!!")
        print('''                ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO\
       ::::::;       ;          OOOOO\
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `# ''')
else:
    print("Your opponent intercepted you with cat like reflexes, then he pinned you to the ground with a barrage of kick and punches... GAME OVER!!!")
    print('''       ___             ___
      //  \           //  \
     //    )         //    )
     ||  _/          ||  _/                   __
     ||  \\_,&__     ||  \\                  (  \
     )|   ^  /  ``---,_\_/ &                 _>  )
     \|___,__\__       `\_  \_              (   /
                \__,-,    `\__\_             >_/
                     \_    /    `\_         / /
                       \_ /        \__    _/ /
                         `\          `\_,/  /
                     _     \__,-,  `   (_  /
                  __( \        ,)__   _/ \/
                 /     `-,___,-'   \_(  O `\
                 \     /_|___   ____/ \  \ =}
                  `---'      `-'       \_=_/{}
                                      .{}{}{}{.
mic                                   {}{}{}{}{
                                      }{}{}{}{}
                                      `}{}{}{}'
                                       `}{}{}''')
