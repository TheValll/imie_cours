package org.imie.fx;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.CheckBox;
import javafx.scene.control.Label;
import javafx.stage.Modality;
import javafx.stage.Stage;

import java.io.IOException;

public class HelloController {
    public CheckBox chkMajuscule;
    public Label lblResult;
    @FXML
    private Label welcomeText;

    @FXML
    protected void onHelloButtonClick() {
        welcomeText.setText("Welcome to JavaFX Application!");
    }

    public void OnOuvrirFenetre(ActionEvent actionEvent) throws IOException {
        FXMLLoader fxmlLoader = new
                FXMLLoader(HelloApplication.class.getResource("Page2.fxml"));
        Scene scene = new Scene(fxmlLoader.load(), 320, 240);
        Stage stage = new Stage();
        stage.setTitle("Page2");
        stage.setScene(scene);
        Page2Controller controller = fxmlLoader.getController();
        controller.setIsMajuscule(chkMajuscule.isSelected());
//controller.txtInput.setText("ABCD");
        stage.initModality(Modality.APPLICATION_MODAL);
        stage.showAndWait();
        lblResult.setText(controller.txtInput.getText());
    }

}