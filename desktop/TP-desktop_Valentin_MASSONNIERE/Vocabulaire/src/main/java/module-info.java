module com.imie.vocabulaire {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.controlsfx.controls;
    requires org.kordamp.bootstrapfx.core;
    requires java.desktop;

    opens com.imie.vocabulaire to javafx.fxml;
    exports com.imie.vocabulaire;
}