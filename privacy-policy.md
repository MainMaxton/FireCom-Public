# FireCom Privacy Policy

Effective date: 1 November 2026

FireCom is a mobile app for fire and emergency crews, developed by Luke Swain in Perth, Western Australia ("we", "us"). This policy explains what personal information the app collects, why, where it is stored, who can see it, how long it is kept, and how you can control or delete it. We aim to comply with the Privacy Act 1988 (Cth) and the Australian Privacy Principles (APPs), and with Apple's App Store Review Guidelines on data collection, use and location services.

## 1. Summary

- We collect only what the app needs to work: accounts, incidents, fire maps, notes and note photos, messages, push notification tokens and the location of truck devices while they are assigned to an open incident.
- Linked crew devices are work devices for fire trucks, set up by the officer in charge (OIC). A truck device shares its location, including in the background, only while the OIC has it assigned to an open incident. Nothing is tracked outside that.
- Everything you add to an incident can be seen only by the OIC who owns it and the OIC's own team.
- We do not sell your information, we do not use it for advertising, and we do not track you across other companies' apps or websites. FireCom contains no advertising, analytics or crash reporting tools.
- You can delete your account and its data inside the app at any time.

## 2. Who uses FireCom

- Officers in charge (OICs) create an account with a name, email address and password. An OIC creates incidents, links truck devices to their team and assigns them to incidents.
- Truck devices (crew devices) are phones or tablets that travel in a fire truck. The OIC sets each one up by joining it to their team with a join code and giving it a name, usually the truck's name. No email address or password is needed; the app creates an anonymous account for the device.

FireCom is meant for use by fire and emergency crews as part of their work. It is not meant for personal phones.

## 3. Information we collect

**Account and profile data**
- OICs: name, email address and password. Passwords are handled by our backend provider (Appwrite) and are stored only in hashed form. We never see your password.
- Truck devices: the device name given at join time or later set by the OIC, the team it belongs to, an anonymous account identifier, and settings the app needs, such as which incident the device is assigned to, when and by whom, and whether the OIC has turned tracking off.
- Sign in sessions.

**Incident data and content you create**
- Incident names and numbers, whether an incident is open or closed, response mode, briefings and incident notes. Notes record the name of the person or device that wrote them and the time. Some notes are added automatically, for example when a truck is assigned, renamed or released, or (if the OIC turns it on) when the wind changes.
- Note photos: photos taken with the camera or chosen from the photo library and attached to a note. Only the photos you choose are uploaded. They are resized on the device before upload.
- Fire maps: fire outlines, sectors, spot fires, arrows, markers and earlier saved versions of each map.
- Brigade points saved by OICs, such as water points and tracks.
- Fire map snapshots: images of a fire map saved to the incident.
- PDF and image reports. These are created on your device, including any note photos, and go only where you choose to send them through your device's share sheet. We do not keep a copy.

**Messages**
- Messages between members of the same team: the sender, the recipient, the sender's name and the message text. A message can be read only by its sender and recipient.

**Push notification data**
- If you allow notifications, a push token for your device, linked to your account, so we can tell you about new messages, assignments and incident activity.

**Location (see section 4)**
- Truck devices assigned to an open incident: coordinates, heading, device name and the time of the last update, plus a breadcrumb trail of recent positions.
- On any device, your coordinates and heading are used on the device for the compass and your own position on the map, and for the local weather shown on the incidents screen (section 4).

**Data stored only on your device**
- The app keeps a local copy of fire maps, queued notes and some settings on the phone so it works with poor reception. Photos you open are cached on the phone. This is cleared when you delete your account or remove the app.

We do not collect contacts, health data, financial information, browsing history, advertising identifiers or analytics data. Photos are only collected when you attach them to a note.

## 4. Location

**Truck devices only.** Location is shared only by truck devices, and only while the OIC has the device assigned to an open incident. The OIC's own location is not sent to anyone.

**Permission.** When a device is set up as a truck, the app explains why it needs location and asks for "While Using the App", then "Always" (iOS) or "Allow all the time" (Android). Location is optional. If it is denied, the rest of the app still works but the truck will not show on the map. You can change or remove the permission at any time in your device settings (iOS: Settings > Privacy & Security > Location Services > FireCom).

**Why background location.** A truck device usually sits locked in the cab. The OIC needs to see where each truck is for crew safety, for example to move trucks out of the way of a fire run or send the nearest truck to a spot fire. Background location lets this work without the screen being on.

**What is sent and when.**
- While assigned to an open incident, the device sends its position about every 20 seconds or when it moves about 25 metres, including in the background. iOS shows the location indicator and Android shows a notification ("Sharing location with command") while this is happening.
- Each position is tagged with the incident the device is assigned to and is shown only on that incident's map.
- The server keeps the latest position and a breadcrumb trail of recent positions (at most about 400 points, never older than 6 hours) so the OIC can see where each truck has been. The map shows the last hour.

**When it stops and is deleted.** Location sharing stops, and the stored position and trail for that device are deleted, when:
- the OIC unassigns the device or turns its tracking off;
- the incident is closed (reopening an incident does not reassign trucks);
- the device is removed from the team, deregistered, or the OIC deletes their account.

Positions and trail points are also deleted automatically once they are more than 6 hours old. If a device stops sending without being unassigned (for example it loses signal), its last position stays on the map with an offline marker until one of the events above or the 6 hour limit. We do not keep any longer location history.

**Weather.** The fire map can show current wind, temperature and humidity for the incident. For this, only the location of the incident's fire map (the centre of the fire edge or a point drawn on the map) is sent to Open-Meteo. No device location, name, account or other personal data is sent with it, and it can be turned off in the map legend. The incidents screen also shows local weather; for that the device's current coordinates are sent to Open-Meteo, again without any name or account details.

**Server checks.** Locations are written only through our server function, which checks on every request that the device is on the team and assigned to that open incident.

## 5. Why we collect it and how we use it (APP 3 and APP 6)

We use personal information only to provide the app's features:
- to create and sign in to accounts;
- to let an OIC and their team share incidents, fire maps, notes, photos, snapshots and messages;
- to show assigned trucks and their recent path on the fire map;
- to show weather and compass information;
- to send notifications about messages, assignments and incident activity; and
- to keep the service secure and working.

We do not use your information for any other purpose, such as marketing, profiling or advertising, unless you agree or the law requires it. We do not sell personal information and we do not share it with data brokers.

## 6. Who can see your information

- Incidents, notes, note photos, fire maps and truck locations and trails: only the OIC who owns the incident and the members of that OIC's team. Note photos are stored with permissions that let only that OIC and team open them.
- Fire map snapshots: the OIC who owns the incident.
- Messages: only the sender and the recipient.
- Names of team members and devices: other members of the same team.
- Service providers listed in section 7, only so far as needed to run the app.
- We may disclose information if required by law, for example under a court order.

Nobody outside the OIC's team can see your data in the app, and we do not otherwise share it with anyone.

## 7. Third party services

FireCom uses these services. Each handles data under its own privacy policy.

- **Appwrite Cloud** (Appwrite Code Ltd): our backend and data processor for accounts, sign in, database, file storage for map snapshots and note photos, and server functions. Our project is hosted in Appwrite's Sydney, Australia region. https://appwrite.io/privacy
- **Apple Maps** (iOS) and **Google Maps** (Android): the base map shown in the app. Your device requests map data for the area you are viewing from Apple or Google.
- **Esri World Imagery** (Esri, with imagery from Maxar and Earthstar Geographics): satellite imagery on the fire map. Your device requests image tiles from Esri's servers (server.arcgisonline.com). These requests reveal the map area you are viewing and your IP address to Esri, but not your name or account. https://www.esri.com/en-us/privacy/overview
- **Open-Meteo**: weather lookups as described in section 4. https://open-meteo.com/en/terms
- **Expo push notification service** (650 Industries, Inc.), which delivers notifications through **Apple Push Notification service** and, on Android, **Firebase Cloud Messaging** (Google). These receive your push token and the notification title and text. https://expo.dev/privacy
- **Expo Application Services (EAS) Update**: the app checks Expo's servers for app updates. This sends technical information such as the app version and platform, not your account data.

We do not use any advertising, analytics, attribution or crash reporting SDKs.

## 8. Where your data is stored and overseas disclosure (APP 8)

Your data, including note photos, is stored with Appwrite Cloud in its Sydney, Australia region and is sent over encrypted connections (HTTPS).

Some of the providers in section 7 are based outside Australia, mainly in the United States, and may process limited data there: Expo, Apple, Google and Esri (push tokens, notification text, map and tile requests and IP addresses) and Open-Meteo (weather lookups, operated from the European Union). We use these providers only for the purposes above.

## 9. Security (APP 11)

We protect your information with encrypted connections, per user and per team access permissions on every record and file, and server side checks on every request for incidents, notes, photos, maps, messages and locations. No system is perfectly secure, but we take reasonable steps to protect your information from misuse, loss and unauthorised access, and we delete it when it is no longer needed.

## 10. How long we keep information

- Accounts, incidents, notes, note photos, fire maps, snapshots and messages: while the OIC's account exists, until deleted.
- Earlier versions of fire maps: removed automatically after 30 days.
- Truck positions and trails: see section 4 (deleted on unassign, tracking off or close, and never kept longer than 6 hours).
- Push tokens: replaced or removed when they stop being valid, when you sign out, or when the account is deleted.
- When an incident is deleted, its notes and every photo attached to them are deleted with it.
- When an account is deleted, its data is removed from our database straight away. Backups held by our hosting provider may take up to 30 days to expire.

## 11. Deleting your account (Apple guideline 5.1.1(v))

You can delete your account inside the app:
- OICs: Profile > Delete account. This permanently deletes your account, all incidents you own with their notes and note photos, fire maps, map versions, snapshots, brigade points, messages, truck locations and trails, push tokens and your team, along with the truck device accounts on your team.
- Truck devices: Profile > Deregister Device. This deletes the device's account, its messages, its location and trail and its push token, and removes it from the team. Notes and photos it added stay part of the OIC's incident record until the OIC deletes them.

Deletion cannot be undone. Data stored only on the phone is cleared when the account is deleted, or you can remove the app.

## 12. Withdrawing consent

You can withdraw consent at any time:
- Location: the OIC can unassign a truck or turn its tracking off, and anyone can remove FireCom's location permission in the device settings.
- Camera and photos: only used when you choose to attach a photo. You can remove access in your device settings.
- Notifications: turn notifications off in your device settings.
- Everything else: delete your account as described in section 11, or contact us.

## 13. Access, correction and deletion (APP 12 and APP 13)

You can see and correct most of your information in the app. You can also ask us to give you a copy of your personal information, correct it, or delete it by emailing us at the address below. We will respond within 30 days. We do not charge for requests. If we refuse a request, we will tell you why and how to complain.

## 14. Children

FireCom is intended for adult fire and emergency crew members. It is not for anyone under 16 and we do not knowingly collect their information. If you believe a child has given us information, contact us and we will delete it.

## 15. Complaints

If you have a concern about how we handle your personal information, please contact us first. We will respond within 30 days. If you are not satisfied with our response, you can complain to the Office of the Australian Information Commissioner (OAIC): www.oaic.gov.au, phone 1300 363 992.

## 16. Changes to this policy (APP 1)

We may update this policy when the app changes. The current version is always available at https://mainmaxton.github.io/FireCom-Public/privacy-policy.html and in the app's App Store listing, with a new effective date.

## 17. Contact

Luke Swain
Perth, Western Australia
Email: bigwaterapps@gmail.com
