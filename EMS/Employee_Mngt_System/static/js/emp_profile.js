// Get the form and buttons
const profileForm = document.getElementById('profileForm');
const editBtn = document.getElementById('editBtn');

// Disable form inputs initially
disableFormInputs();

// Add event listener to the Edit button
editBtn.addEventListener('click', enableFormInputs);

// Add event listener to the form submission
profileForm.addEventListener('submit', saveProfile);

// Function to disable form inputs
function disableFormInputs() {
  const inputs = profileForm.querySelectorAll('input, select, textarea');
  inputs.forEach(input => {
    input.disabled = true;
  });
}

// Function to enable form inputs
function enableFormInputs() {
  const inputs = profileForm.querySelectorAll('input, select, textarea');
  inputs.forEach(input => {
    input.disabled = false;
  });
}

// Function to save the profile
function saveProfile(event) {
  event.preventDefault();
  
  // Get the form values
  const employeeId = document.getElementById('employeeId').value;
  const firstName = document.getElementById('firstName').value;
  const lastName = document.getElementById('lastName').value;
  const department = document.getElementById('department').value;
  const email = document.getElementById('email').value;
  const mobile = document.getElementById('mobile').value;
  const aadhar = document.getElementById('aadhar').value;
  const gender = document.getElementById('gender').value;
  const dob = document.getElementById('dob').value;
  const currentAddress = document.getElementById('currentAddress').value;
  const residentialAddress = document.getElementById('residentialAddress').value;
  const dateOfJoining = document.getElementById('dateOfJoining').value;
  const salary = document.getElementById('salary').value;
  const cv = document.getElementById('cv').value;
  const photo = document.getElementById('photo').value;
  const status = document.getElementById('status').value;
  const leave = document.getElementById('leave').value;
  const retair = document.getElementById('retair').value;
  const transfer = document.getElementById('transfer').value;
  
  // Perform validation if needed
  
  // Save the profile data (you can send it to a server or store it locally)
  console.log('Employee ID:', employeeId);
  console.log('First Name:', firstName);
  console.log('Last Name:', lastName);
  console.log('Department:', department);
  console.log('Email:', email);
  console.log('Mobile Number:', mobile);
  console.log('Aadhar Number:', aadhar);
  console.log('Gender:', gender);
  console.log('Date of Birth:', dob);
  console.log('Current Address:', currentAddress);
  console.log('Residential Address:', residentialAddress);
  console.log('Date of Joining:', dateOfJoining);
  console.log('Salary:', salary);
  console.log('CV:', cv);
  console.log('Photo:', photo);
  console.log('Status:', status);
  console.log('Leave:', leave);
  console.log('Retair:', retair);
  console.log('Transfer:', transfer);
  
  // Disable form inputs after saving
  disableFormInputs();
}
