import Login from "./login";
import Enzyme from "enzyme";
import { render, screen, fireEvent } from "@testing-library/react";
import Adapter from "enzyme-adapter-react-16";
import React from "react";
import { MemoryRouter } from "react-router";
import { mount } from "enzyme";

Enzyme.configure({ adapter: new Adapter() });

describe("routes using memory router", () => {
  it("should show Login component for / router (using memory router)", () => {
    const component = mount(
      <MemoryRouter initialentries="{['/login']}">
        <Login />
      </MemoryRouter>
    );
    expect(component.find(Login)).toHaveLength(1);
  });
});

test("render username", () => {
  render(<Login />);
  expect(screen.getByText(/Username/)).toBeInTheDocument();
});

test("render password", () => {
  render(<Login />);
  expect(screen.getByText(/Password/)).toBeInTheDocument();
});

it("submits", () => {
  const handleSubmit = jest.fn();
  const { getByText } = render(<Login handleSubmit={handleSubmit} />);
  fireEvent.submit(getByText("Submit"));
  expect(handleSubmit).toHaveLength(0);
});
