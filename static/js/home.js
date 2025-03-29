/**
 * Handles form submission
 * @param {Event} event - The event object from form submission
 */
const handleSubmit = async (event) => {
  event.preventDefault();

  const toast = new ToastNotifier({
    position: "top-right", // Default position
  });
  const formData = new FormData(event.target);
  const jsonData = JSON.stringify(Object.fromEntries(formData.entries()));

  /** @type {import('axios').AxiosInstance} */
  axios
    .post("/create_booking", jsonData, {
      headers: {
        "Content-Type": "application/json",
      },
    })
    .then((response) => {
      toast.success("Successfully Booked an appointment. Check your email!");

      console.log(response.data);
    })
    .catch((error) => {
      toast.error("Error creating booking. Please try again.");
      console.error(error);
    });
};
