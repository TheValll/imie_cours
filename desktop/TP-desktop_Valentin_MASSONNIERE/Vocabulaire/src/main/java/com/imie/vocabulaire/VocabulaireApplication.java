package com.imie.vocabulaire;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;
import java.util.List;

public class VocabulaireApplication extends Application {
    @Override
    public void start(Stage stage) throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(VocabulaireApplication.class.getResource("vocabulaire-view.fxml"));
        Scene scene = new Scene(fxmlLoader.load(), 600, 300);
        stage.setTitle("Vocabulary game!");

        ReadCsv.WordPair wordPair = ReadCsv.getLanguageWords("src/main/resources/com/imie/vocabulaire/data.csv");
        List<String> randomLanguage1Words = wordPair.randomLanguage1Words();
        List<String> language2Words = wordPair.language2Words();
        List<String> language2Good = wordPair.language2Good();

        System.out.println("Mots aléatoires (Langue 1) : " + randomLanguage1Words);
        System.out.println("Mots corrects (Langue 2) : " + language2Good);
        System.out.println("Mots (Langue 2) : " + language2Words);

        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch();
    }
}
