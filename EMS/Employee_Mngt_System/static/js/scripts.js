// event_app/static/js/scripts.js
function submitEvent() {
    const eventName = document.getElementById('id_eventName').value;
    const eventDate = document.getElementById('id_eventDate').value;
    const eventVenue = document.getElementById('id_eventVenue').value;
    const eventDescription = document.getElementById('id_eventDescription').value;
    const certificateUpload = document.getElementById('id_certificateUpload').value;

    const newEvent = document.createElement('div');
    newEvent.innerHTML = `<strong>${eventName}</strong> - ${eventDate} - ${eventVenue} - ${eventDescription}`;

    document.getElementById('event-container').appendChild(newEvent);

    // Clear the form
    document.getElementById('event-form').reset();
}
