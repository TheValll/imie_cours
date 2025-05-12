package org.imie.fx;

import java.awt.*;
import java.awt.event.ActionEvent;

public class Page2Controller {
    public javafx.scene.control.TextArea txtInput;
    private boolean isMajuscule=false;
    public void setIsMajuscule(boolean isMajuscule) {
        this.isMajuscule = isMajuscule;
    }

    public void OnAction(javafx.event.ActionEvent actionEvent) {
        if (this.isMajuscule)
            txtInput.setText(txtInput.getText().toUpperCase());
        else
            txtInput.setText(txtInput.getText().toLowerCase());
    }
}