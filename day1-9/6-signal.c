#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#define FILENAME "6-input.txt"
#define GROUPSIZE 4
#define GROUP2SIZE 14

bool no_repeat_in_group(char* buf, int size) {
	//printf("Checking group: %s ",buf);
    for (int i=0; i<size; ++i) {
        for (int j=i+1;j<size;++j) {
            if (*(buf+j)==*(buf+i)) { // repeat found
                //printf(" repeat found at %d\n",j);
                return false; 
            }
        }
    }
	return true;
}

int main() {
    FILE* fileptr;
    int filesize;
    char* buffer;
    char group[GROUPSIZE];
    char group2[GROUP2SIZE];
 
    // Opening file in reading mode
    fileptr = fopen(FILENAME, "r");
 
    if (!fileptr) {
        printf("file can't be opened \n");
        return 1;
    }
 
    // check file size
    fseek(fileptr, 0, SEEK_END); // seek to end of file
    filesize = ftell(fileptr); // get current file pointer
    fseek(fileptr, 0, SEEK_SET); // seek back to beginning of file

    // allocate memory
    buffer=malloc(filesize*sizeof(char));

    // read file
    fgets(buffer,filesize,fileptr);
 
    // look for transmission
    for (int i=0; ;++i) {  // no boundary checking here!     
        if (i+GROUPSIZE>filesize) { // cannot make group
            printf("Reached EOF, group not found\n");
            return 2;
        }
        strncpy(group,buffer+i,GROUPSIZE);
        if (no_repeat_in_group(group,GROUPSIZE)) {
			printf("\nBegin transmission found at %d\n",i+GROUPSIZE);
			break;
		}
    }

    // look for message
    for (int i=0; ;++i) {  // no boundary checking here!
        if (i+GROUP2SIZE>filesize) { // cannot make group
            printf("Reached EOF, group not found\n");
            return 2;
        }
        strncpy(group2,buffer+i,GROUP2SIZE);
        if (no_repeat_in_group(group2,GROUP2SIZE)) {
			printf("\nBegin message found at %d\n",i+GROUP2SIZE);
			break;
		}
    }


    // Cleanup
    free(buffer);
    fclose(fileptr);
    return 0;
}
