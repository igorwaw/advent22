#include <stdio.h>
#include <stdlib.h>
//#include <string.h>
//#include <stdbool.h>

#define FILENAME "8-small.txt"
//#define FILENAME "8-input.txt"

void error(int nr) {
    switch(nr)
    {
        case 1: printf("file can't be opened \n"); break;
        default: printf("unknown error: %d",nr);
    }
    exit(nr);
}

int get_cols(FILE* file) {
    char c;
    int cols=0;
    while ( (c=getc(file)) != EOF ) {
        if (c=='\n')
            break;
        ++cols;
    }
    fseek(file, 0, SEEK_SET); // seek back to beginning of file
    return cols;
}

int read_contents(FILE* file, char* buf, int rows, int cols) {
    for (int i=0;i<rows;++i) {
        fgets( (buf+i*cols), cols+2, file );
        printf("Reading row %d: %s\n", i, (buf+i*cols) );
    }
}

void print_contents(char* buf, int rows, int cols) {
    puts("DEBUG: printing buffer\n");
    for (int i=0;i<rows;++i) {
        printf("%d ",i);
        for (int j=0; j<cols; ++j)
            putchar( *(buf+i*cols+j) );
        puts("\n");
    }
}

int count_visible(char* buf, int rows, int cols) {
    // first and last row/column are visible
    // -4 because corners would be counted twice without it
    int visible=cols*2+rows*2-4; 
    for (int i=1; i<rows-1; ++i) { // skip first and last row here
        for (int j=1; j<cols-1; ++j) { // skip first/last columns
            char c=*(buf+i*cols+j);
        }
    }
    return visible;
}


int main() {
    FILE* fileptr;
    char* buffer;
    int filesize,numrows,numcols,visible;

    
    fileptr = fopen(FILENAME, "r"); // Opening file in reading mode
    if (!fileptr) 
        error(1);
     
    // check file size
    fseek(fileptr, 0, SEEK_END); // seek to end of file
    filesize = ftell(fileptr); 
    fseek(fileptr, 0, SEEK_SET); // seek back to beginning of file
    numcols=get_cols(fileptr);
    numrows=filesize/(numcols+1); // +1 for \n at the end of every line


    buffer=malloc(filesize*sizeof(char));
    read_contents(fileptr,buffer,numrows,numcols);
    //print_contents(buffer, numrows, numcols);   // for debug only
    visible=count_visible(buffer, numrows, numcols);

    printf("filename %s size %d rows %d cols %d visible trees %d\n", FILENAME, filesize, numrows, numcols, visible);

     // Cleanup
    free(buffer);
    fclose(fileptr);
    return 0;
}