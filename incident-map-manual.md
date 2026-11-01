# Incident map manual

FireCom Incident Manager for iOS

The fire map is a shared satellite map for one incident. Everyone on the OIC's team sees the same drawing. Changes save and sync on their own. If you lose signal, changes wait on the device and upload when you are back online.

To open it, open the incident and tap **Start fire shape** or **Edit fire shape**, or swipe the incident left and tap **Fire map**. Closed incidents open view only.

## 1. The screen

**Top bar**

- **Back**: leave the map.
- **History**: saved versions of the map.
- **Filter**: choose what shows on the map.
- **Export**: PDF report or map image.
- **Ruler**: measure distances.
- **Settings**: Map settings (appliances and crew edit permissions).
- **Clear**: wipe the drawing. Crew see **Locked** unless the OIC allows it. On a view only map this shows **View only**.

**Left side**

- **Legend**, with the **Trails** and **Weather** switches.
- The weather card, when weather is on.
- The north button. Tap it to turn the map back to north up.

**Bottom panel**

- The tool row: **Fire edge**, **Spot fire**, **Points**, **Sector**, **Tracks** (OIC only), **Arrow** and **Select**. Swipe the row to see them all.
- A hint line that tells you the next step.
- **Grid**, **Undo**, **Redo**, **Note**, and a save or delete button for the current tool.
- Tap the arrow at the top of the panel to hide it or bring it back.

## 2. Fire edge

The fire edge is the main outline of the fire.

1. Tap **Fire edge**.
2. Tap the map at each corner of the fire.
3. When you have at least 3 corners, tap the save button to close the edge.

To change it later:

1. Tap **Edit**.
2. Drag corners to new spots. Tap a corner and confirm to remove it.
3. Tap **Done** to save, or **Cancel** to put it back as it was.

The map shows the edge length and burnt area while **Measurements and labels** is on.

## 3. Spot fires

1. Tap **Spot fire**.
2. Tap around the spot fire to outline it.
3. Tap the first corner again, or tap the save button, to finish. You need at least 3 corners.

Spot fires are named *Spot 1*, *Spot 2* and so on. To resize one, drag its corners while in Spot fire mode. Tap a spot fire to see its area or delete it.

## 4. Points

1. Tap **Points**.
2. Pick a type: Water point, Entry point, Hazard, Control Point, Assembly point, Bulk water, Point of origin or Asset at Risk.
3. For **Asset at Risk**, also pick what is at risk: House, Building, Power line, Water, Road/Bridge or Other.
4. Tap the map to drop the point.

To edit a point, tap it. Add a short note (up to 120 characters, for example *20k L tank, gate code 1234*) and tap **Done**, or tap **Remove**. To move a point, hold it and drag.

## 5. Sectors

Sectors split the fire edge into named stretches. Draw the fire edge first. Sectors are made from its corners.

### Smart sectors

When part of the edge has no sector yet, FireCom shows a **+** on it.

1. Tap **Sector**.
2. Tap a **+** to make a sector from that free stretch.
3. Name it (for example *Sector A* or *Northern flank*). The OIC can also add a **Radio channel**.
4. Tap **Save**.

### Pick your own corners

1. Tap **Sector**.
2. Tap the fire edge corner where the sector starts.
3. Tap the corner where it ends.
4. Two ways round the edge are shown as **A** and **B**. Tap the one this sector covers.
5. Name it and tap **Save**.

New sectors get the next free letter (*Sector A*, *Sector B* and so on). A stretch can only belong to one sector.

### Change a sector

1. In Sector mode, tap the sector's name.
2. Choose **Start** or **End** to move that end, **Edit** to rename it or change its radio channel, or **Close**.
3. To move an end, tap a ringed corner, then tap the tick to save. If this opens a gap next to another sector, FireCom asks if that sector should move to close it. Choose **No** to leave the gap free.
4. To delete the sector, tap the bin at the top right and confirm.

## 6. Arrows

1. Tap **Arrow**.
2. Pick **Wind direction** or **Fire direction**.
3. Tap where the arrow starts, then where it points.

Tap an arrow to select it. Then tap **Delete**, or tap Wind or Fire to change its type.

## 7. Tracks (OIC only)

Tracks mark roads and firebreaks.

1. Tap **Tracks**.
2. Tap along the map to draw the track.
3. Tap **Save track**. Tap **Done** when finished.

Tap a track to edit it. Add a short note, tag it **LT Only** or **4WD Only** (or both), then **Save**, or tap **Remove**.

## 8. Select

Use Select to move or delete several corners at once.

1. Tap **Select**.
2. Tap corners to select them.
3. Drag one selected corner to move them all, or tap **Delete**.

## 9. Undo, redo, grid and note

- **Undo** and **Redo** step back and forward through your changes.
- **Grid** snaps new corners to a grid. Tap again to turn it off. To see the grid itself, turn on **Grid** in **Filter**.
- **Note** adds a note about the fire shape, up to 500 characters. Tap **Done** to save.

## 10. Briefing and command channel

The briefing and command channel belong to the incident, not the drawing. The OIC edits them in **Incident details** by tapping the pencil. Crew see the command channel as a badge on the incident and in details. Clearing the map does not remove the briefing.

## 11. Legend, layers and weather

### Legend

The legend lists what is on the map. Tap the up arrow to hide it, and **Legend** to show it again. If anything is hidden by Filter, the legend shows how many.

- Tap **Trails** to show or hide truck trails.
- Tap **Weather** to show or hide the weather card.

FireCom remembers your Trails and Weather choice next time.

### Filter

1. Tap **Filter**.
2. Turn items on or off: Fire edge, Spot fires, Sectors, each point type, Tracks, Wind arrows, Fire arrows, Crew vehicles, Truck trails, Weather, Measurements and labels, and Grid.
3. Tap **Done**.

Filter only changes what you see and export. Nothing is deleted. Grid starts hidden.

### Weather card

The weather card shows wind direction and speed, gusts, temperature and humidity for the map area. The wind arrow turns orange at 40 km/h or more. If nothing is drawn yet it says **Draw on the map for weather**.

On an open incident the OIC can turn on **Log changes**. FireCom then adds a note to the activity log when the wind swings 45 degrees or more, or rises to 40 km/h or more.

## 12. Truck markers and trails

- Each assigned truck shows as a coloured marker. Each truck keeps its own colour. Tap a marker to see its name and when it last updated.
- Each truck has a trail of its path over the last hour, in the truck's colour. Older parts of the trail are fainter.
- If a truck has not sent a position for about a minute, its marker turns grey with an **Appliance offline** badge. Tap it to see when it was last located, for example *Last located 7:42pm, 2h ago*.
- A truck's last known spot stays on the map for up to 6 hours, then it is removed.
- When the OIC unassigns a truck or turns its tracking off, its marker is removed.

Truck positions update about every 20 seconds while the map is open.

<h2 id="appliances">13. Map settings</h2>

Tap **Settings** at the top of the map.

### Appliances

Lists every truck on the team with its status: **Not assigned**, **Assigned to** another incident, **Assigned here**, or **Assigned here, tracking off**.

The OIC can:

1. Tap **Assign here** to put a truck on this incident. If it is on another incident, confirm **Move**.
2. Tap **Unassign** to take it off.
3. Use the switch to turn tracking on or off for a truck assigned here.

A truck device shows *This phone is* and its name. Only the OIC chooses its incident.

### Crew can edit

The OIC can turn crew editing on or off for this map only:

- Fire edge, Spot fires, Points, Sectors, Wind arrows, Fire arrows, Briefing and channel, Activity log notes: on unless you turn them off.
- Clear map: off unless you turn it on.

Locked tools show a lock and **Locked by OIC** for crew. The server keeps locked items as they are, so crew changes cannot overwrite them. Crew can see these settings but not change them.

Tap **Done** to close.

## 14. History

Each saved version of the map is kept.

1. Tap **History**.
2. Tap a version to view it. The map shows **Viewing version** and its number.
3. The OIC can tap **Restore** to make that version current.
4. Tap **Back to current** or **Close** to leave.

History needs signal.

## 15. Ruler

1. Tap **Ruler**.
2. Tap the map to add points. The card shows the total distance and the last leg.
3. Use undo to remove the last point, **Clear** to start again, and **Done** to finish.

## 16. Export and map pictures

1. Tap **Export**.
2. Choose **PDF report** or **Map image**.
3. Wait while the map picture is built, then share it from the share sheet.

The picture is the satellite map with the drawing on top. Items hidden with Filter are left out, and the PDF says how many were hidden. Each export saves the picture as the incident's map snapshot. A snapshot is also saved when the incident is closed. The PDF from **Incident details** uses the latest snapshot if it is up to date with the drawing.

## 17. Clear the map

1. Tap **Clear**.
2. Confirm **Clear**.

This removes the fire edge, spot fires, points, sectors, arrows and the shape note. The briefing stays. Crew can only do this if the OIC has turned on **Clear map**.

## More

- [Operating FireCom](operating-firecom.html)
- [Privacy policy](privacy-policy.html)
- [Support](index.html)
