#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

char board[3][3] = { 
    {'-', '-', '-'}, 
    {'-', '-', '-'}, 
    {'-', '-', '-'}
};

// Player pawns
const char FIRST_PLAYER = 'X';
const char SECOND_PLAYER = 'O';


bool check_for_win() {

    for (int i = 0; i <= 2; i++) {


        // Checks row
        if ( board[i][0] == board[i][1] && board[i][0] == board[i][2] && board[i][0] != '-' ) {

            return 1;


        // Checks column
        } else if ( (board[0][i] == board[1][i] && board[0][i] == board[2][i] && board[0][i] != '-') ) {

            return 1;

        }
    }

    // Checks cross
    if ( board[0][0] == board[1][1] && board[0][0] == board[2][2] && board[0][0] != '-' ) {

        return 1;

    } else if ( board[0][2] == board[1][1] && board[0][2] == board[2][0] && board[0][2] != '-' ) {

        return 1;
        
    }


    return 0;

}


void showBoad() {

    // https://iq.opengenus.org/detect-operating-system-in-c/
    // System specific clear

    #ifdef _WIN32 // For Windows
        system("cls");
    #endif

    #ifdef __linux__ //For Linux
        system("clear");
    #endif


    printf("  1|2|3\n");
    printf("1|%c|%c|%c\n", board[0][0], board[0][1], board[0][2]);
    // printf("-----\n");
    printf("2|%c|%c|%c\n", board[1][0], board[1][1], board[1][2]);
    // printf("-----\n");
    printf("3|%c|%c|%c\n", board[2][0], board[2][1], board[2][2]);
    
}

int main() {
    
    char player = FIRST_PLAYER;
    // showBoad();

    // printf("%i\n",checkRow(first_row));
    // printf("%i\n",checkColumn());

    while ( true ) {
        

        

        int row;
        int column;

        showBoad();
        printf("Place %c\n", player);

        // https://stackoverflow.com/questions/25034298/why-would-scanf-make-my-switch-statement-freak-out
        // For it to not freak out with the printf statement, you need to use %u in scanf because int is undefined

        printf("Row: ");
        scanf("%u", &row);
        printf("Column: ");
        scanf("%u", &column);
        
        // Changes on board
        row -= 1;
        column -= 1;

        if ( board[row][column] == '-' ) {

            board[row][column] = player;

        } else {
            // Added so that no turns is skipped due to placed on already placed square
            continue;

        }

        



        // Checks for winner combinations
        if (check_for_win()) {
            showBoad();
            printf("%c WON!\n", player);
            break;

        }


        // Switches player
        if ( player == FIRST_PLAYER ) {

            player = SECOND_PLAYER;

        } else if ( player == SECOND_PLAYER ) {

            player = FIRST_PLAYER;

        }

    }
    
}