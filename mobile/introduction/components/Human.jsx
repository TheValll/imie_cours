import { StyleSheet, Text, View, Image } from "react-native";
import { sty } from "../app.style.js";
// export function Human(props) {
//   console.log(props);
//   return (
//     <>
//       <Text style={{ fontSize: 20 }}>
//         Je suis {props.firstName}
//         {props.lastName} j'ai {props.age} ans et je possède une{" "}
//         {props.car.brand}
//         et sa vitesse maximale est de {props.car.maxSpeed} milliard de km/h
//       </Text>
//       <Image
//         style={{ height: 200, width: 200, margin: 30 }}
//         source={{
//           uri: "https://cdn.betterttv.net/emote/65d944345858fd5b7280440d/3x.webp",
//         }}
//       />
//     </>
//   );
// }

export function Human({ firstName, lastName, age, car, children }) {
  return (
    <>
      <View style={sty.rectangle}>
        <Text style={{ fontSize: 20, marginTop: 30 }}>
          Je suis {lastName} {firstName} et j'ai {age} ans
        </Text>
        <Text style={{ fontSize: 20 }}>
          Ma voiture est une {car.brand} elle roule au max à {car.maxSpeed}{" "}
          milliard de km/h
        </Text>
      </View>
      {children}
    </>
  );
}
