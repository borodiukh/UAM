#include <stdio.h>
#include <stdlib.h>
#include <unistd.h> // getcwd, chdir, fork()
#include <string.h> // strtok, strcmp
#include <sys/types.h> // for fork()
#include <sys/wait.h> // for wait()


int main()
{
    char path[200]; // max lenght of path
    char table[200]; // for fgets, strtok
    char *piece;
    char *argument[20]; // table of commands from stdin
    int i; // counter
    char copypath[100] = "";
    
while(1) // infinity loop
{
    if(getcwd(path, 200)) // write home path into variable 'path'
    {
        printf("[%s] %s $ ", path, getenv("USER"));
        fgets(table, 200, stdin); // read data from stdin and write it in table
        
        piece = strtok(table, " \t\n"); // string token
        
        for(i = 0; i < 20 && piece != NULL; i++)
        {
            argument[i] = piece;
            piece = strtok(NULL, " \t\n");
        }
        argument[i] = NULL;
        
        if(argument[0] == NULL) // if stdin is empty
        {
            continue;
        }
        else if(strcmp(argument[0], "exit") == 0)
        {
            exit(0);
        }
        else if(strcmp(argument[0], "help") == 0)
        {
            printf("Project was created by Yurii Borodiukh\n");
            printf("Available commands: exit, help, cd\n");
        }
        else if(strcmp(argument[0], "cd") == 0)
        {
            if(argument[1] == NULL)
            {
                getcwd(copypath, 200);
                chdir(getenv("HOME"));
                
            }
            else if(strcmp(argument[1], "~") == 0)
            {
                getcwd(copypath, 200);
                chdir(getenv("HOME"));
            }
            else if(strcmp(argument[1], "-") == 0)
            {
                chdir(copypath);
            }
            else
            {
                getcwd(copypath, 200);
                chdir(argument[1]);
            }
        }
        else
        {
            int id = fork();
            if(id == 0)
            {
                execvp(argument[0], argument); // if command is available run it
                printf("The command cannot be executed\n");
                return 0;
            }
            else
            {
                wait(0); // parent proces is waiting for a child execution
                // parent proces doing nothing
            }
        }
        
    }
    
    else
    {
        perror("getcwd() error");
        return 1;
    }
}

return 0;
}

