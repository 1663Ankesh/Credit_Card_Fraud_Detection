const express = require("express");
const bodyParser = require("body-parser");
const axios = require("axios");

const app = express();
const port = 3000;

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.get("/", (req, res) => {
  res.sendFile(__dirname + "/Form.html");
});

app.post("/predict", async (req, res) => {
  const csvInput = req.body.csv_input;

  const values = csvInput.split(",").map(parseFloat);

//   console.log(values);

  try {
    const response = await axios.post("http://127.0.0.1:5000/predict", {
      data: values,
    });
    console.log(response.data);
    const prediction = response.data;
    res.json(prediction);
  } catch (error) {
    console.error("Error making API call:", error.message);
    res.status(500).json({ error: "Internal Server Error" });
  }
});

app.listen(port, () => {
  console.log(`Server is running on ${port}`);
});
