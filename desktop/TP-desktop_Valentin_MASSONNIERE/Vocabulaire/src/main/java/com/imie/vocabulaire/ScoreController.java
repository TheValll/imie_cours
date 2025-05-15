package com.imie.vocabulaire;

import javafx.fxml.FXML;
import javafx.scene.control.TextField;

public class ScoreController {
    @FXML
    private TextField scoreLabel;

    public void setText(String str1, String str2, int number){
        scoreLabel.setText("Good job " + str1 + " " + str2 + " Your score is " + number);
    }
}
