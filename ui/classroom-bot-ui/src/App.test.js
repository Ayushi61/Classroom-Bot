import React from "react";
import {
  render,
  screen,
  fireEvent,
  cleanup,
  waitForElement,
  getByTitle,
} from "@testing-library/react";
import ReactDOM from "react-dom";
import App from "./App";
import TopBar from "./common/topBar";
//import Body from "./common/body";

test("renders code flow", async () => {
  const { debug } = render(<App />);
  debug();
});
test("renders home page", async () => {
  const { getByText } = render(<App />);
  getByText("This is main");
});

test("render topbar", () => {
  render(<TopBar />);
  expect(screen.getByText(/Classroom Slack Bot - Admin/)).toBeInTheDocument();
});

const links = [
  { text: "Classroom Slack Bot - Admin", location: "/" },
  { text: "Commands", location: "/commands" },
  { text: "Data Source", location: "/datasource" },
];
// I use test.each to iterate the test cases above
test.each(links)("Check if Nav Bar have %s link.", (link) => {
  render(<TopBar />);
  //Ensure the text is in the dom, will throw error it can't find
  const linkDom = screen.getByText(link.text);

  //use jest assertion to verify the link property
  expect(linkDom).toHaveAttribute("href", link.location);
});

//test("render body", () => {
//render(<Body />);
//expect(screen.getByText(/Classroom Slack Bot - Admin/)).toBeInTheDocument();
//});
