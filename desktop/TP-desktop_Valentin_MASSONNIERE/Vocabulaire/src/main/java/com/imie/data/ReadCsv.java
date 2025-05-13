package com.imie.data;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public class ReadCsv {

    public record WordPair(List<String> randomLanguage1Words, List<String> language2Words, List<String> language2Good) {
    }

    public static WordPair getLanguageWords(String filePath) {
        List<String> language2Words = new ArrayList<>();
        List<String> language1Words = new ArrayList<>();
        List<String> randomWords = new ArrayList<>();
        List<String> language2Good = new ArrayList<>();

        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] parts = line.split(";");
                if (parts.length == 2) {
                    language1Words.add(parts[0].trim());
                    language2Words.add(parts[1].trim());
                }
            }

            List<String> tempLanguage1Words = new ArrayList<>(language1Words);
            List<String> tempLanguage2Words = new ArrayList<>(language2Words);

            if (!tempLanguage1Words.isEmpty()) {
                randomWords.add(tempLanguage1Words.remove(0));
                language2Good.add(tempLanguage2Words.remove(0));

                Random random = new Random();
                while (randomWords.size() < 15 && !tempLanguage1Words.isEmpty()) {
                    int index = random.nextInt(tempLanguage1Words.size());
                    randomWords.add(tempLanguage1Words.remove(index));
                    language2Good.add(tempLanguage2Words.remove(index));
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        return new WordPair(randomWords, language2Words, language2Good);
    }
}
