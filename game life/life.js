class GameOfLife {
    constructor(num_of_rows, num_of_columns) {

        this.num_rows = num_of_rows;
        this.num_columns = num_of_columns;

        this.nextFieldInd = 1;
        this.curFieldInd = 0;

        // 1st field for show, 2nd field for $подсчёт$,
        // after $подсчёт$ their indexes changes with each other
        this.fields = new Array(2);
        this.fields[0] = new Array(this.num_rows);
        this.fields[1] = new Array(this.num_columns);

        for (let field_i = 0; field_i < 2; ++field_i) {
            for (let row_id = 0; row_id < num_of_rows + 2; ++row_id) {
                let row = new Array(num_of_columns + 2);
                row.fill(false);
                this.fields[this.curFieldInd][row_id] = row;
            }
        }
    }
    

    changeCell(i, j) {
        this.fields[this.curFieldInd][i][j] = !(this.fields[this.curFieldInd][i][j]);
    }

    isAlive(i, j) {
        return this.fields[this.curFieldInd][i][j];
    }
 
    initializeBlinker() {
        this.fields[this.curFieldInd][4][5] = true;
        this.fields[this.curFieldInd][5][5] = true;
        this.fields[this.curFieldInd][6][5] = true;
    }
 
    initializeGlider() {
        this.fields[this.curFieldInd][3][4] = true;
        this.fields[this.curFieldInd][4][5] = true;
        this.fields[this.curFieldInd][5][3] = true;
        this.fields[this.curFieldInd][5][4] = true;
        this.fields[this.curFieldInd][5][5] = true;
    }



    getAliveNeighbs(i, j) {
        let aliveNeighbs = 0;
        for (let di = -1; di < 2; ++di) {
            for (let dj = -1; dj < 2; ++dj) {
                if (this.fields[this.curFieldInd][i + di][j + dj]) ++aliveNeighbs;
            }
        }
        if (this.fields[this.curFieldInd][i][j]) {--aliveNeighbs;}
        return aliveNeighbs;
    }

    UpdateNextFieldCenter() {
        for (let i = 1; i < this.num_rows + 1; ++i) {
            for (let j = 1; j < this.num_columns + 1; ++j) {
                let aliveNeighbs = this.getAliveNeighbs(i, j);

                if (this.fields[this.curFieldInd][i][j]) {
                    if (aliveNeighbs < 2 | aliveNeighbs > 3) this.fields[this.nextFieldInd][i][j] = false;
                    else this.fields[this.nextFieldInd][i][j] = true; 
                } else {
                    if (aliveNeighbs == 3) this.fields[this.nextFieldInd][i][j] = true;
                    else this.fields[this.nextFieldInd][i][j] = false;
                }
            }
        }
    }

    UpdateNextFieldEdges() {
                
        // up and down without angles
        for (const i of [0, this.num_rows + 1]) {
            for (let j = 1; j < this.num_rows + 1; ++j) {
                this.fields[this.nextFieldInd][i][j] = this.fields[this.nextFieldInd][Math.abs(i - this.num_rows)][j];
            }
        }

        // right and left without angles
        for (const j of [0, this.num_rows + 1]) {
            for (let i = 1; i < this.num_rows + 1; ++i) {
                this.fields[this.nextFieldInd][i][j] = this.fields[this.nextFieldInd][i][Math.abs(j - this.num_columns)];
            }
        }

        // angles
        for (const i of [0, this.num_rows + 1]) {
            for (const j of [0, this.num_rows + 1]) {
                this.fields[this.nextFieldInd][i][j] = this.fields[this.nextFieldInd][Math.abs(i - this.num_rows)][Math.abs(j - this.num_columns)];
            }
        }
    }

    doStep() {
        this.UpdateNextFieldCenter();
        this.UpdateNextFieldEdges();

        this.curFieldInd = this.nextFieldInd;
        this.nextFieldInd = (this.nextFieldInd + 1) % 2;
    }
}