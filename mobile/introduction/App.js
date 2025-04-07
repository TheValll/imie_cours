import { StatusBar } from "expo-status-bar";
import { StyleSheet, Text, View, ScrollView, Image } from "react-native";
import { Human } from "./components/Human";
import { Pot } from "./components/Pot";
import { SafeAreaProvider } from "react-native-safe-area-context";
import { SafeAreaView } from "react-native";
import { sty } from "./app.style.js";

export default function App() {
  return (
    <SafeAreaProvider>
      <View style={styles.container}>
        <ScrollView>
          <Pot />
          <Human
            lastName={"Valssim"}
            firstName={"Bessonière"}
            age={44}
            car={{ brand: "Toyota AE86 ", maxSpeed: 230 }}
            isHappy={true}
            doSomething={() => {
              console.log("Passage dans doSomeThing");
            }}
          >
            <Image
              style={{ height: 300, width: 300, marginTop: 30 }}
              source={{
                uri: "https://cdn.betterttv.net/emote/65d944345858fd5b7280440d/3x.webp",
              }}
            />
          </Human>
          <StatusBar style="auto" />
        </ScrollView>
      </View>
    </SafeAreaProvider>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
    padding: 20,
    marginTop: 50,
  },
});
