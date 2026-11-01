# Operating FireCom

FireCom Incident Manager for iOS

This guide covers setting up FireCom as an officer in charge (OIC), running incidents, and using the truck devices that travel in your appliances. For drawing on the fire map, see the [Incident map manual](incident-map-manual.html).

## 1. Who does what

- **OIC.** Has an email and password account. Creates incidents, owns the team, links truck devices, names them and assigns them to incidents.
- **Truck device.** A phone or tablet that lives in a fire truck. It joins the OIC's team with an invite code. FireCom treats every linked crew device as a truck (an appliance). It shares its location only while the OIC has it assigned to an open incident.

## 2. Set up as the OIC

### Create your account

1. Open FireCom and tap **Register as an OIC**.
2. Enter a username, email address and password, then confirm the password.
3. Register. You land on **My Incidents**.

Next time, tap **Login as an OIC** on the home screen.

To change your display name, email or password, open the **Profile** tab and tap the settings (gear) button at the top. Your current password is only needed to change your email or password. A new password must be at least 8 characters.

### Make an invite code

1. Open the **Profile** tab.
2. Under **Invite code**, tap the generate button. A new 6 letter code appears.
3. Give the code to whoever is setting up the truck device.

Tapping generate again replaces the code. To stop a code working, tap the bin next to it and confirm **Erase invite code**. Devices already linked stay linked.

### Link a truck device

FireCom links devices by typing the invite code. There is no QR code option.

On the truck's phone:

1. Open FireCom and tap **Join a team**.
2. Enter the 6 letter code from the OIC and tap **Continue**.
3. Under **Identify this device**, enter a name, for example *Light Tanker 1*, and tap **Join team**.
4. The first time the device finds out it is a truck, FireCom shows **Set up** with the device name. Tap **Continue**, choose **Allow While Using App**, then **Change to Always Allow**. You can tap **Not now**, but background sharing will not work until Always is allowed.

Back on the OIC's phone, open **Profile** and tap the refresh button next to **Linked crew**. The new device shows in the list.

### Rename a truck

1. In **Profile > Linked crew**, tap the round **...** button on the truck's row.
2. Tap **Rename**.
3. Enter the new name, for example *Pumper 1*, and save.

### Assign a truck to an incident

1. In **Profile > Linked crew**, tap the round **...** button on the truck's row.
2. Tap **Assign**.
3. Pick an open incident from the **Assign** list. The current one has a tick.

The row then shows **Assigned:** and the incident. A truck is on one incident at a time. If no incidents are open, the list says **No open incidents**.

You can also assign, move or unassign trucks from inside the fire map. See *Appliances* in the [Incident map manual](incident-map-manual.html#appliances).

### Remove a device from the team

1. In **Profile > Linked crew**, tap the bin on the device's row.
2. Confirm **Remove**. The device is signed out and needs a new code to join again.

## 3. Incidents

### Create an incident

1. On **My Incidents**, tap the add button.
2. Enter the **Incident ID** and **Incident name**. An **Opening note** is optional.
3. Pick the **Response**: *Normal Road* or *Emergency Conditions*.
4. Tap **Create incident**.

### Find and open incidents

- Use the **Active** and **Closed** tabs to switch lists. Tap refresh to reload.
- Tap an incident to open **Incident details**.
- Hold an active incident to set it as your active job. Your quick notes go to that job.
- Swipe an incident left for more: **Set active** or **Unset**, **Fire map**, and **Close**. On a closed incident: **View map** and **Re-open**.

### Incident details

From **Incident details** you can:

- Open the fire map. The button reads **Start fire shape**, **Edit fire shape**, or on a closed incident **View fire shape**.
- Export a PDF report.
- Close or open the incident.
- Change the **Response** mode.
- Read and edit the briefing and command channel. Tap the pencil to edit. Every briefing change is also written to the activity log.
- Read and add to the **Activity log**.

### Close an incident

1. Open **Incident details**, or swipe the incident left.
2. Tap **Close incident** (or **Close**) and confirm.

When an incident closes:

- All crew and trucks are released from it. Trucks show **Not assigned** and stop sharing their location.
- Crew no longer see it as active. The fire map becomes view only.
- A final map picture is saved for the report.
- Note photos are deleted 28 days after closing. Closed incidents with photos show how many days are left in the activity log.

### Reopen an incident

1. Open the **Closed** tab.
2. Swipe the incident left and tap **Re-open**, or open it and tap **Open incident**. Confirm.

Reopening does not put any crew or trucks back on it. Assign them again from **Profile** or the map. Reopening also stops the 28 day photo countdown. If you close it again, the 28 days start again from that close.

## 4. Notes and photos

### Quick notes

The **Quick notes** buttons add a set message to your active job, for example *Turning out to incident.*, *Arrived at incident.*, *On fireground.* or *Released from incident.*

1. Hold an active incident to make it your active job.
2. Tap a quick note button.
3. Check the preview and tap **Confirm**.

### Custom notes

1. Open **Incident details**.
2. Tap **Add custom note**.
3. Type your note.
4. To add photos, use the camera button to take one or the library button to pick some. Up to 4 photos per note. Tap the cross on a photo to remove it.
5. Tap **Add note**, check the preview and tap **Confirm**.

Things to know:

- Notes and photos can be seen by the OIC and everyone on the OIC's team.
- Photos are resized and saved as JPEG before upload.
- Photos are included in PDF reports.
- If there is no signal, the note is saved on the device and uploads when you are back online. You will see **Saved on this device**.
- After the 28 days, a note keeps its text and shows *Photos removed 28 days after the incident closed*.
- The OIC can lock the activity log for crew in the map's **Map settings**. Crew then see **Notes are locked by the OIC for this incident.**

## 5. Messages

Messages are private chats between two members of the same team.

As the OIC:

1. Open **Profile**.
2. Tap the chat bubble on a device's row. A dot on the bubble means unread messages.
3. Type up to 200 characters and send.

On a truck device:

1. Open the **Profile** tab.
2. Under **Linked crew**, tap the chat bubble next to the OIC (or another device) and send your message.

## 6. Push notifications

FireCom asks for notification permission so it can tell you about new messages. When a message arrives you get a notification titled *Message from* and the sender's name. Tap it to open that chat.

If you turn notifications off, messages still arrive. You just will not be alerted.

## 7. PDF report

1. Open **Incident details**.
2. Tap the export button.
3. Wait for the report to build, then share or save it from the share sheet.

The report includes the incident, the briefing, the fire map picture and the activity log, with note photos (up to 40 photos per report).

You can also export from inside the fire map. Tap **Export**, then **PDF report** or **Map image**.

## 8. Location sharing

### When a truck shares its location

A truck device sends its location only when all of these are true:

- the OIC has assigned it to an incident,
- that incident is open, and
- the OIC has not turned its tracking off in **Map settings**.

It sends about every 20 seconds, or when it moves about 25 metres. With **Always** allowed, it keeps sending when the phone is locked or FireCom is in the background. With **While Using App** only, it sends while FireCom is open.

Sharing stops when the incident closes, the truck is unassigned, tracking is turned off, or the device is deregistered.

The OIC's own phone never shares its location. The OIC's phone uses location only on the device for the compass heading, local weather and the blue dot on the map. Tap **Enable location** on **My Incidents** if it is off.

### How to tell if a device is sharing

A truck device always shows a small banner at the top of the screen:

- **Assigned to:** and the incident name, or **Not assigned**.
- **Sharing location**, only while it is actually sharing.

When FireCom is in the background and sharing, iOS shows its own blue location indicator.

## 9. Deregister a device or delete an account

### Deregister a truck device

On the truck's phone:

1. Open the **Profile** tab.
2. Tap **Deregister Device**.
3. Read the warning and confirm.

The device leaves the team, and its crew account and messages are deleted. It needs a new invite code to join again.

### Delete an OIC account

1. Open **Profile** and tap the settings (gear) button.
2. Tap **Want to delete your account? Click here**.
3. Read what will be deleted.
4. Tick **I understand all incidents and data will be deleted**.
5. Type **DELETE** and tap **Delete forever**.

This permanently deletes all your incidents and notes, invite codes, messages, push tokens and your team. Every device that joined with your code loses access and its crew account is removed. It cannot be undone. With no signal, nothing is deleted.

## 10. Permissions

FireCom asks for:

- **Location, While Using App.** Compass heading, local weather and your position on the map. On a truck device, also its position for the OIC.
- **Location, Always.** Truck devices only. Lets the truck keep sharing while the phone is locked, during an assigned open incident only.
- **Camera** and **Photos.** Only when you add a photo to a note.
- **Notifications.** Message alerts.

Each one is optional. If you say no, the rest of the app keeps working.

### Change or revoke a permission

1. Open the iPhone **Settings** app.
2. Scroll down and tap **FireCom**.
3. Change **Location** (Never, Ask Next Time, While Using the App, or Always), **Photos**, **Camera** or **Notifications**.

## More

- [Incident map manual](incident-map-manual.html)
- [Privacy policy](privacy-policy.html)
- [Support](index.html)
