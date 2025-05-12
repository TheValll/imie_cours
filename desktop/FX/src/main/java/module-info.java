module org.imie.fx {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.controlsfx.controls;
    requires org.kordamp.bootstrapfx.core;
    requires java.desktop;

    opens org.imie.fx to javafx.fxml;
    exports org.imie.fx;
}