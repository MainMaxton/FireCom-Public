# FireCom Privacy Policy

Effective date: 30 October 2026

FireCom is a mobile app for fire and emergency crews, developed by Luke Swain in Perth, Western Australia ("we", "us"). This policy explains what personal information the app collects, why, where it is stored, who can see it, how long it is kept, and how you can control or delete it. We aim to comply with the Privacy Act 1988 (Cth) and the Australian Privacy Principles (APPs), and with Apple's App Store Review Guidelines on data collection, use and location services.

## 1. Summary

- We collect only what the app needs to work: your account, your incidents, fire maps, notes and messages, a push notification token and, for crew who allow it, their location during an active incident.
- Location is used only while the app is open in the foreground. FireCom asks for "While Using the App" (When In Use) permission only. It never asks for "Always" or background location permission and never collects location in the background.
- Crew locations are visible only to the officer in charge (OIC) and crew of the incident, only while that incident is active, and crew can switch sharing off at any time.
- We do not sell your information, we do not use it for advertising, and we do not track you across other companies' apps or websites. FireCom contains no advertising, analytics or crash reporting tools.
- You can delete your account and its data inside the app at any time.

## 2. Who uses FireCom

There are two kinds of users:

- Officers in charge (OICs) create an account with a name, email address and password. An OIC creates incidents and invites crew.
- Crew (contributors) join an OIC's team with a join code and a name. Crew do not give an email address or password; the app creates an anonymous account for them.

## 3. Information we collect

**Account and sign in data**
- OICs: name, email address and password. Passwords are handled by our backend provider (Appwrite) and are stored only in hashed form. We never see your password.
- Crew: the name you enter, an optional callsign or role, the team you joined, and an anonymous account identifier.
- Sign in sessions and account settings (for example whether Share my location is on).

**Incident data and content you create**
- Incident names, whether an incident is active or closed, and incident notes.
- Fire maps: fire outlines, sectors, spot fires, markers and earlier saved versions of each map.
- Brigade points saved by OICs, such as water points and tracks, with an optional short note.
- Fire map snapshots: images of a fire map saved to the incident.
- Reports you export (PDF or image) are created on your device and shared only where you choose to send them through your device's share sheet.

**Messages**
- Messages between members of the same team: the sender, the recipient, the sender's name and the message text. A message can be read only by its sender and recipient.

**Push notification data**
- If you allow notifications, a push token for your device, linked to your account, so we can tell you about new messages and incident activity.

**Location (see section 4)**
- Your device's coordinates and heading, used on the device for the compass, weather and your own position on the fire map.
- If Share my location is on: coordinates, heading, name, role and time of the last update, for the active incident whose fire map you opened last. We keep one record per account per incident, and each update overwrites it.

**Data stored only on your device**
- The app keeps a local copy of your fire maps and some settings on your phone so it works with poor reception. This is removed when you delete your account or remove the app.

We do not collect contacts, photos from your library, health data, financial information, browsing history, advertising identifiers or analytics data.

## 4. Location

**Permission.** FireCom asks for location permission "While Using the App" only (iOS When In Use; on Android, foreground location only). It never requests "Always" or background location, and it does not collect location when the app is closed or in the background. Location is optional: if you deny it, everything else in the app still works.

**What it is used for.**
- Compass heading and your own position on the fire map. This stays on your device.
- Local weather. Your coordinates are sent to Open-Meteo to look up the forecast. Open-Meteo does not receive your name or account details.
- Crew vehicle positions on the fire map, described below.

**Crew location sharing.**
- Your location is shared only when the Share my location switch is on.
- It is shared only while FireCom is open in the foreground. This can be on any screen in the app, not just the fire map. It is shared for the active incident whose fire map you opened last. Updates are sent about every 20 seconds or when the device moves about 25 metres.
- It stops straight away when the app goes to the background or closes, when you turn the switch off, or when the incident is no longer active, and your position is removed from the map.
- Crew locations can be seen only by the OIC who owns the incident and the crew on that OIC's team who can open the incident. They are not public and are not shown to anyone else. Anyone removed from the team stops seeing locations and their own location is removed.
- Locations are read and written only through our server function, which checks these rules on every request. There is no direct access to the location records from the app.

**Opting out.** You can turn off "Share my location" in the fire map settings at any time. When it is off, the app stops sending location, your stored location is deleted, and the server refuses any further location from that account, even from an older version of the app. You can also remove FireCom's location permission at any time in your device settings (iOS: Settings > Privacy & Security > Location Services > FireCom).

**How long location is kept.** We store one location record per account per incident. Each update overwrites it, so only your latest position is kept. It is deleted:
- when you turn off Share my location, or when the app goes to the background or closes;
- when the incident is deleted; and
- when your account is deleted. When an OIC deletes their account, their incidents and the data linked to them, including crew locations, are deleted too.

There is no scheduled or automatic clean up job. We do not keep a location history or trail.

## 5. Why we collect it and how we use it (APP 3 and APP 6)

We use personal information only to provide the app's features:
- to create and sign in to accounts;
- to let an OIC and their crew share incidents, fire maps, notes, snapshots and messages;
- to show crew vehicles on the fire map during an active incident;
- to show weather and compass information;
- to send notifications about messages and incident activity; and
- to keep the service secure and working.

We do not use your information for any other purpose, such as marketing, profiling or advertising, unless you agree or the law requires it. We do not sell personal information and we do not share it with data brokers.

## 6. Who can see your information

- Incidents, fire maps, notes and snapshots: the OIC who owns the incident and the crew on that OIC's team.
- Crew locations: as described in section 4.
- Messages: only the sender and the recipient.
- Your name or callsign: other members of your team.
- Service providers listed in section 7, only so far as needed to run the app.
- We may disclose information if required by law, for example under a court order.

We do not otherwise share your information with anyone.

## 7. Third party services

FireCom uses these services. Each handles data under its own privacy policy.

- **Appwrite Cloud** (Appwrite Code Ltd): our backend for accounts, sign in, database, file storage for map snapshots, and server functions. Our project is hosted in Appwrite's Sydney, Australia region. https://appwrite.io/privacy
- **Apple Maps** (iOS) and **Google Maps** (Android): the base map shown in the app. Your device requests map data for the area you are viewing from Apple or Google.
- **Esri World Imagery** (Esri, with imagery from Maxar and Earthstar Geographics): satellite imagery on the fire map. To show it, your device requests image tiles from Esri's servers (server.arcgisonline.com). These requests reveal the map area you are viewing and your IP address to Esri, but not your name or account. https://www.esri.com/en-us/privacy/overview
- **Open-Meteo**: weather lookups using your coordinates, as described in section 4. https://open-meteo.com/en/terms
- **Expo push notification service** (650 Industries, Inc.), which delivers notifications through **Apple Push Notification service** and, on Android, **Firebase Cloud Messaging** (Google). These receive your push token and the notification title and text. https://expo.dev/privacy
- **Expo Application Services (EAS) Update**: the app checks Expo's servers for app updates. This sends technical information such as the app version and platform, not your account data.

We do not use any advertising, analytics, attribution or crash reporting SDKs.

## 8. Where your data is stored and overseas disclosure (APP 8)

Your data is stored with Appwrite Cloud in its Sydney, Australia region and is sent over encrypted connections (HTTPS).

Some of the providers in section 7 are based outside Australia, mainly in the United States, and may process limited data there: Expo, Apple, Google and Esri (push tokens, notification text, map and tile requests and IP addresses) and Open-Meteo (weather lookups, operated from the European Union). We use these providers only for the purposes above and choose providers that publish privacy commitments.

If you choose to connect FireCom to your own self managed Appwrite server, your data is stored on that server instead and you are responsible for it.

## 9. Security (APP 11)

We protect your information with encrypted connections, per user access permissions in the database, and server side checks on every request for incidents, maps, messages and locations. Crew location records cannot be read directly by the app at all. No system is perfectly secure, but we take reasonable steps to protect your information from misuse, loss and unauthorised access, and we delete it when it is no longer needed.

## 10. How long we keep information

- Account, incidents, fire maps, notes, snapshots and messages: while your account exists, until you or the OIC delete them.
- Earlier versions of fire maps: removed automatically after 30 days.
- Crew locations: see section 4. Only the latest position is kept, and it is usually removed as soon as the app leaves the foreground.
- Push tokens: replaced or removed when they stop being valid, when you sign out, or when your account is deleted.
- When an account is deleted, its data is removed from our database straight away. Backups held by our hosting provider may take up to 30 days to expire.

## 11. Deleting your account (Apple guideline 5.1.1(v))

You can delete your account inside the app:
- OICs: Profile (settings) > Delete account. This permanently deletes your account, all incidents you own, their fire maps, map versions, snapshots, notes, brigade points, messages, crew locations, push tokens and your team, along with the crew accounts on your team.
- Crew: Profile > Deregister Device. This deletes your crew account, your messages, your locations and your push token, and removes you from the team.

Deletion cannot be undone. Data stored only on your phone is cleared when you delete your account, or you can remove the app.

## 12. Withdrawing consent

You can withdraw consent at any time:
- Location: turn off Share my location (crew) and/or remove location permission in your device settings.
- Notifications: turn notifications off in your device settings.
- Everything else: delete your account as described in section 11, or contact us.

Withdrawing consent does not affect the rest of the app, except the features that need that data.

## 13. Access, correction and deletion (APP 12 and APP 13)

You can see and correct most of your information in the app. You can also ask us to give you a copy of your personal information, correct it, or delete it by emailing us at the address below. We will respond within 30 days. We do not charge for requests. If we refuse a request, we will tell you why and how to complain.

## 14. Children

FireCom is intended for adult fire and emergency crew members. It is not directed at children under 16 and we do not knowingly collect their information. If you believe a child has given us information, contact us and we will delete it.

## 15. Complaints

If you have a concern about how we handle your personal information, please contact us first. We will respond within 30 days. If you are not satisfied with our response, you can complain to the Office of the Australian Information Commissioner (OAIC): www.oaic.gov.au, phone 1300 363 992.

## 16. Changes to this policy (APP 1)

We may update this policy when the app changes. The current version is always available at https://mainmaxton.github.io/FireCom-Public/privacy-policy.html and in the app's App Store listing, with a new effective date.

## 17. Contact

Luke Swain
Perth, Western Australia
Email: bigwaterapps@gmail.com
