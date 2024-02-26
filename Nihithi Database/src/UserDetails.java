
import java.util.Map;
import java.util.List;
public class UserDetails {
    private Map<String, String> bodyMeasurements; // Map to store AR-generated measurements
    private List<String> occasion;
    private List<String> skinTone;

    public Map<String, String> getBodyMeasurements() {
        return bodyMeasurements;
    }

    public void setBodyMeasurements(Map<String, String> bodyMeasurements) {
        this.bodyMeasurements = bodyMeasurements;
    }

    public List<String> getOccasion() {
        return occasion;
    }

    public void setOccasion(List<String> occasion) {
        this.occasion = occasion;
    }

    public List<String> getSkinTone() {
        return skinTone;
    }

    public void setSkinTone(List<String> skinTone) {
        this.skinTone = skinTone;
    }

    public class ARMeasurementCapture {
        public Map<String, String> captureMeasurements() {
            // Your AR measurement capture logic here
            // For example, you might use a library or device-specific APIs
            // to obtain measurements and return them as a map
            // Replace the following line with your actual implementation
            // This is just an illustrative example.
            return obtainARMeasurements();
        }

        private Map<String, String> obtainARMeasurements() {
            // Replace this with your actual logic to obtain AR measurements
            // For now, using a dummy map as an example
            return Map.of("Bust", "36", "Waist", "28", "Hip", "38");
        }
    }

    ARMeasurementCapture arMeasurementCapture = new ARMeasurementCapture();
    Map<String, String> arMeasurements = arMeasurementCapture.captureMeasurements();

    UserInfo userInfo = new UserInfo();
    userInfo.setBodyMeasurements(arMeasurements);

    userInfo.setOccasions(Arrays.asList("Casual", "Formal", "Party", "Semi-formal"));

    userInfo.setSkinTones(Arrays.asList("Fair", "Dark", "Light", "Brown"));
}
