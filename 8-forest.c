#include <stdio.h>
#include <stdlib.h>

//#define FILENAME "8-small.txt"
#define FILENAME "8-input.txt"



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

void print_contents(char* buf, int rows, int cols) {
    puts("DEBUG: printing buffer\n");
    for (int i=0;i<rows;++i) {
        printf("%d ",i+1);
        for (int j=0; j<cols; ++j)
            putchar( *(buf+i*cols+j) );
        putchar('\n');
    }
}

int count_visible(char* buf, int rows, int cols) {
    int num_visible=0;
    char* visiblebuf=calloc(rows*cols, sizeof(char) ); // visible trees will be saved here
    // malloc leaves random content, calloc sets to 0
    inline void add_visible(int a, int b) { *(visiblebuf+a*cols+b)+=1; }

    char cur_max; // will hold largest value (highest tree) seen in the iteration
    char c; // height of the current tree

    // first and last row visible
    for (int j=0;j<=cols-1;++j) {
        add_visible(0,j);
        add_visible(rows-1,j);
    }

    // first and last column visible
    for (int i=0;i<=rows-1;++i) {
        add_visible(i,0);
        add_visible(i,cols-1);
    } 

    /*
    The code below counts from how many directions the tree is visible.
    We only need to check if it's visible from at least 1 direction.
    It's very inefficienet, there's really no need to store array of visible
    trees. But I thought it might be useful for part2.
    In the hindsight, I should have used similar algorithm as in check_score
    */

    // begin iterate rows then columns
    for (int i=0; i<=rows-1; ++i) { // iterate rows
        for (int j=0; j<=cols-1; ++j) { // iterate columns left to right, skip last, don't skip first
            c=*(buf+i*cols+j);
            if (j==0)
                cur_max=c;
            else {
                if (c>cur_max) { // tree is visible
                    //printf("Tree at %d,%d height %d (max %d) visible from the left\n", i+1, j+1, c-48, cur_max-48 ); //debug
                    add_visible(i,j);
                    cur_max=c;
                }
            }
        } // end iterate columns left to right
        for (int j=cols-1; j>=0; --j) { // iterate columns right to left, skip like above
            c=*(buf+i*cols+j);
            if (j==cols-1)
                cur_max=c;
            else {
                if (c>cur_max) { // tree is visible
                    //printf("Tree at %d,%d height %d (max %d) visible from the right\n", i+1, j+1, c-48, cur_max-48 ); //debug
                    add_visible(i,j);
                    cur_max=c;
                }
            }
        } // end iterate columns right to left
    } // end iterate rows then columns

    // begin iterate columns then rows
    for (int j=0; j<=cols-1; ++j) { // iterate columns
        for (int i=0; i<=rows-1; ++i ) { // iterate rows to to bottom, skip last, don't skip first
            c=*(buf+i*cols+j);
            if (i==0)
                cur_max=c;
            else {
                if (c>cur_max) { // tree is visible
                    //printf("Tree at %d,%d height %d (max %d) visible from the top\n", i+1, j+1, c-48, cur_max-48 ); //debug
                    add_visible(i,j);
                    cur_max=c;
                }
            }
        } // end iterate rows top to bottom
        for (int i=rows-1; i>=0; --i) { // iterate rows bottom to top
            c=*(buf+i*cols+j);
            if (i==rows-1)
                cur_max=c;
            else {
                if (c>cur_max) { // tree is visible
                    //printf("Tree at %d,%d height %d (max %d) visible from the bottom\n", i+1, j+1, c-48, cur_max-48 ); //debug
                    add_visible(i,j);
                    cur_max=c;
                }
            }
        } // end iterate rows bottom to top 
    } // end iterate columns then rows

    // count trees marked as visible
    for (int x=0;x<rows*cols;++x) {
        if (*(visiblebuf+x)>0)
            ++num_visible;
    }
    free(visiblebuf);
    return num_visible;
}

int check_score(char* buf, int cur_row, int cur_col, int rows, int cols) {
    if (cur_row==0 || cur_row==rows-1 || cur_col==0 || cur_col==cols-1) // tree on the edge
        return 0;

    char current_tree=*(buf+cur_row*cols+cur_col); // height of the current tree
    char other_tree;
    int scoreleft=0;
    int scoreright=0;
    int scoretop=0;
    int scorebottom=0;
    // check score to the left
    for (int j=cur_col-1; j>=0; --j) {
        ++scoreleft;
        other_tree=*(buf+cur_row*cols+j);
        //printf(" left: %d",other_tree-48);
        if (other_tree>=current_tree) // view is blocked
            break;
    }
     // check score to the right
    for (int j=cur_col+1; j<rows; ++j) {
        ++scoreright;
        other_tree=*(buf+cur_row*cols+j);
        //printf(" right: %d",other_tree-48);
        if (other_tree>=current_tree)
            break;
    } 
    // check score to the top
    for (int i=cur_row-1; i>=0; --i) {
        ++scoretop;
        other_tree=*(buf+i*cols+cur_col);
        //printf(" top: %d",other_tree-48);
        if (other_tree>=current_tree)
            break;
    }
    // check score to the bottom
    for (int i=cur_row+1; i<cols; ++i) {
        ++scorebottom;
        other_tree=*(buf+i*cols+cur_col);
        //printf(" bottom: %d",other_tree-48);
        if (other_tree>=current_tree)
            break;
    }
    // done checking
    int score=scoreleft*scoreright*scoretop*scorebottom;
    //printf("\nChecking tree at %d,%d height %d score %d (%d,%d,%d,%d)\n\n", cur_row+1, cur_col+1, current_tree-48, score, scoretop, scoreleft, scoreright, scorebottom);
    return score;
}

int get_score(char* buf, int rows, int cols) {
    int highest_so_far=0;
    int score=0;
    for (int i=0; i<rows; ++i) {
        for (int j=0; j<cols; ++j) {
            score=check_score(buf, i, j, rows, cols);
            if (score>highest_so_far)
                highest_so_far=score;
        }
    }
    return highest_so_far;
}

int main() {
    FILE* fileptr;
    char* filecontents;
    int filesize,numrows,numcols,visible,highscore;

    
    fileptr = fopen(FILENAME, "r"); // Opening file in reading mode
    if (!fileptr) {
        printf("file can't be opened \n");
        return 1;
    }
     
    // check file size
    fseek(fileptr, 0, SEEK_END); // seek to end of file
    filesize = ftell(fileptr); 
    fseek(fileptr, 0, SEEK_SET); // seek back to beginning of file
    numcols=get_cols(fileptr);
    numrows=filesize/(numcols+1); // +1 for \n at the end of every line


    filecontents=malloc(filesize*sizeof(char));
    
    
    for (int i=0;i<numrows;++i)
        fgets( (filecontents+i*numcols), numcols+2, fileptr );
    //print_contents(filecontents, numrows, numcols);   // for debug only
    visible=count_visible(filecontents, numrows, numcols);
    highscore=get_score(filecontents, numrows, numcols);

    printf("filename %s size %d rows %d cols %d visible trees %d highest score %d\n", FILENAME, filesize, numrows, numcols, visible, highscore);

     // Cleanup
    free(filecontents);
    fclose(fileptr);
    return 0;
}