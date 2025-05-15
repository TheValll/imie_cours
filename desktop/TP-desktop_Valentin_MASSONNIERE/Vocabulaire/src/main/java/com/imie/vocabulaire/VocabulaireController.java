package com.imie.vocabulaire;

import com.imie.data.ReadCsv;
import javafx.beans.property.SimpleStringProperty;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.stage.FileChooser;
import javafx.stage.Modality;
import javafx.stage.Stage;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
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
    private TextField firstName;

    @FXML
    private TextField lastName;

    private static final List<String> globalSelectedChoices = new ArrayList<>();
    private static final List<String> globalAnswers = new ArrayList<>();

    public void updateTableView(ReadCsv.WordPair wordPair) {
        List<String> randomLanguage1Words = wordPair.randomLanguage1Words();
        List<String> language2Words = wordPair.language2Words();
        List<String> language2Good = wordPair.language2Good();
        globalAnswers.addAll(language2Good.subList(1, language2Good.size()));

        ObservableList<String> language2GoodObservables = FXCollections.observableArrayList(language2Words.subList(1, language2Words.size()));
        languageView.getItems().clear();

        firstNameColumn.setText(randomLanguage1Words.getFirst());
        secondNameColumn.setText(language2Good.getFirst());
        firstNameColumn.setCellValueFactory(cellData -> new SimpleStringProperty(cellData.getValue().getWord()));

        secondNameColumn.setCellFactory(col -> {
            return new TableCell<WordChoicePair, String>() {
                @Override
                protected void updateItem(String item, boolean empty) {
                    super.updateItem(item, empty);
                    if (empty) {
                        setGraphic(null);
                    } else {
                        WordChoicePair pair = getTableView().getItems().get(getIndex());
                        ChoiceBox<String> choiceBox = new ChoiceBox<>(language2GoodObservables);
                        choiceBox.setPrefWidth(col.getWidth());

                        if (pair.getChoiceBox().getValue() != null) {
                            choiceBox.getSelectionModel().select(pair.getChoiceBox().getValue());
                        }

                        choiceBox.getSelectionModel().selectedItemProperty().addListener((observable, oldValue, newValue) -> {
                            pair.setChoiceBox(choiceBox);
                        });

                        setGraphic(choiceBox);
                    }
                }
            };
        });

        for (int i = 1; i < randomLanguage1Words.size(); i++) {
            String mot = randomLanguage1Words.get(i);
            ChoiceBox<String> choiceBox = new ChoiceBox<>(language2GoodObservables);
            WordChoicePair pair = new WordChoicePair(mot, choiceBox);
            languageView.getItems().add(pair);
        }
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
    private void handleOpenFile() {
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

    @FXML
    private void handleCheckTraduction() throws IOException {
        ObservableList<WordChoicePair> score = languageView.getItems();
        String userFirstName = firstName.getText();
        String userLastName = lastName.getText();

        for (WordChoicePair pair : score) {
            String word = pair.getWord();
            ChoiceBox<String> choiceBox = pair.getChoiceBox();
            String selectedChoice = choiceBox.getValue();
            globalSelectedChoices.add(selectedChoice);
        }

        Integer userScore = ReadCsv.getScore(getGlobalSelectedChoices(), getGlobalAnswers());
        newWindow(userFirstName, userLastName, userScore);
        handleReplay();
    }

    @FXML
    private void handleReadScore() {
    }

    @FXML
    private void handleReplay() {
        languageView.getItems().clear();
        firstName.clear();
        lastName.clear();
        firstNameColumn.setText("Language 1");
        secondNameColumn.setText("Language 2");
        globalSelectedChoices.clear();
        globalAnswers.clear();
    }

    public static List<String> getGlobalSelectedChoices() {
        return globalSelectedChoices;
    }

    public static List<String> getGlobalAnswers() {
        return globalAnswers;
    }

    public void newWindow(String str1, String str2, int number) throws IOException{
        FXMLLoader fxmlLoader = new FXMLLoader(VocabulaireApplication.class.getResource("score.fxml"));
        Scene scene = new Scene(fxmlLoader.load(), 320, 240);
        Stage stage = new Stage();
        stage.setTitle("User Score Page");
        stage.setScene(scene);
        ScoreController controller = fxmlLoader.getController();
        controller.setText(str1,str2, number);
        stage.initModality(Modality.APPLICATION_MODAL);
        stage.showAndWait();
    }
}
