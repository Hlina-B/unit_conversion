Unit Conversion Web Client (Frontend)
A sleek, responsive, single-page web user interface modeled directly after Google Search's intuitive unit converter layout. Built entirely with semantic HTML5, modern vanilla JavaScript (ES6+), and styled dynamically using Bootstrap 5, this client interfaces natively with the local Flask conversion engine.

Key Features
Google-Style Layout: Parallel input/output cards featuring split configuration select panels for rapid data tracking.

Instant Network Syncing: Eliminates redundant "Submit" or "Convert" buttons. The user interface updates the calculation output in real time upon detecting any user modifications via text input changes or select change switches.

Cascading Dropdowns: Dynamically repopulates corresponding unit conversion lists (Length, Weight, Temperature, Area, etc.) using clean data manifests matching the exact nomenclature configuration of the backend Python Enums.

Client-Side Regex Safeguard: Pre-filters inputs using precise float matching constraints to prevent throwaway characters or unparsed string fragments from causing unnecessary network overhead.

Getting Started & Usage
Save the Client Interface:
Ensure the index.html markup file is safely resting in your designated frontend directory workspace.

Verify the Backend Base URL Endpoint:
Inside the <script> configuration block of your index.html, double-check that your active backend routing network port corresponds accurately:

JavaScript
const API_BASE_URL = "http://127.0.0.1:8080/convert";
Launch the User Interface:
Because this client runs entirely on client-side native web APIs (fetch, URLSearchParams), there is zero local build compilation or bundling required. Simply double-click the index.html file or drag it directly into any internet browser (Chrome, Firefox, Safari) to launch it instantly.

Component Lifecycle & Data Pipeline
The frontend handles communication loops via asynchronous promise execution queues:

Category Selection (#categorySelect): Fires an initialization routine that clears and inserts new localized HTML <option> fragments mapped from the data manifest. It automatically updates indices so that different units are selected on either side by default (e.g., Meter to Centimeter).

Input Interception (#fromValue):
Monitors keystroke buffers. If the text input strings validate against the operational regex:

Code snippet
/^-?\d+(\.\d+)?$/
it safely strips trailing whitespaces and prepares the transmission query parameters string.

Fetch Pipeline:
Dispatches a clean GET protocol request carrying the active state properties directly over to the Flask backend workspace, mapping down the converted numeric return instantly to populate the readonly target result input field.