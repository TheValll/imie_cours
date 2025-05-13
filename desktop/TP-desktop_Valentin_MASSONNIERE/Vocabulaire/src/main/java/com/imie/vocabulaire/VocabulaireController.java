package com.imie.vocabulaire;

import com.imie.data.ReadCsv;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.scene.control.*;
import javafx.stage.FileChooser;

import java.io.File;
import java.util.List;

public class VocabulaireController {

    @FXML
    private TableView<WordChoicePair> languageView;

    @FXML
    private TableColumn<WordChoicePair, String> firstNameColumn;

    @FXML
    private TableColumn<WordChoicePair, String> secondNameColumn;

    @FXML
    private Button openFile;

    @FXML
    private Button readScore;

    @FXML
    public void updateTableView(ReadCsv.WordPair wordPair){
        List<String> randomLanguage1Words = wordPair.randomLanguage1Words();
        List<String> language2Words = wordPair.language2Words();
        List<String> language2Good = wordPair.language2Good();

        ObservableList<String> language2GoodObservables = FXCollections.observableArrayList(language2Words);
        languageView.getItems().clear();

        firstNameColumn.setText(randomLanguage1Words.getFirst());
        secondNameColumn.setText(language2Good.getFirst());
        firstNameColumn.setCellValueFactory(cellData -> new javafx.beans.property.SimpleStringProperty(cellData.getValue().getWord()));

        secondNameColumn.setCellFactory(col -> {
            return new TableCell<WordChoicePair, String>() {
                @Override
                protected void updateItem(String item, boolean empty) {
                    super.updateItem(item, empty);
                    if (empty) {
                        setGraphic(null);
                    } else {
                        ChoiceBox<String> choiceBox = new ChoiceBox<>(language2GoodObservables);
                        choiceBox.getSelectionModel().select(item);
                        choiceBox.setPrefWidth(col.getWidth());
                        setGraphic(choiceBox);
                    }
                }
            };
        });


        for(int i = 1; i < randomLanguage1Words.size(); i++){
            String mot = randomLanguage1Words.get(i);
            ChoiceBox<String> choiceBox = new ChoiceBox<>(language2GoodObservables);
            WordChoicePair pair = new WordChoicePair(mot, choiceBox);
            languageView.getItems().add(pair);
        }

//        System.out.println("Mots aléatoires (Langue 1) : " + randomLanguage1Words);
//        System.out.println("Mots corrects (Langue 2) : " + language2Good);
//        System.out.println("Mots (Langue 2) : " + language2Words);
    }

    public static class WordChoicePair {
        private String word;
        private ChoiceBox<String> choiceBox;

        public WordChoicePair(String word, ChoiceBox<String> choiceBox) {
            this.word = word;
            this.choiceBox = choiceBox;
        }

        public String getWord() {
            return word;
        }

        public void setWord(String word) {
            this.word = word;
        }

        public ChoiceBox<String> getChoiceBox() {
            return choiceBox;
        }

        public void setChoiceBox(ChoiceBox<String> choiceBox) {
            this.choiceBox = choiceBox;
        }
    }

    @FXML
    private void handleOpenFIle(){
        FileChooser fileChooser = new FileChooser();
        fileChooser.setTitle("Open a CSV file");

        FileChooser.ExtensionFilter filter = new FileChooser.ExtensionFilter("CSV File", "*.csv");
        fileChooser.getExtensionFilters().add(filter);

        File selectedFile = fileChooser.showOpenDialog(openFile.getScene().getWindow());

        if (selectedFile != null) {
            ReadCsv.WordPair wordPair = ReadCsv.getLanguageWords(selectedFile.getAbsolutePath());
            updateTableView(wordPair);
        }
    }
}