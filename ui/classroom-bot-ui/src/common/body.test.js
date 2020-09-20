import React from "react";
import {
  render,
  screen,
  fireEvent,
  cleanup,
  waitForElement,
  getByTitle,
} from "@testing-library/react";
import { MemoryRouter } from "react-router";
import { shallow, mount } from "enzyme";
import Main from "../main/main";
import Enzyme from "enzyme";
import Adapter from "enzyme-adapter-react-16";
import Datasource from "../main/datasource";
Enzyme.configure({ adapter: new Adapter() });

describe("routes using memory router", () => {
  it("should show Main component for / router (using memory router)", () => {
    const component = mount(
      <MemoryRouter initialentries="{['/']}">
        <Main />
      </MemoryRouter>
    );
    expect(component.find(Main)).toHaveLength(1);
  });
});

describe("routes using memory router", () => {
  it("should show Main component for / router (using memory router)", () => {
    const component = mount(
      <MemoryRouter initialentries="{['/main']}">
        <Main />
      </MemoryRouter>
    );
    expect(component.find(Main)).toHaveLength(1);
  });
});

//describe("routes using memory router", () => {
//it("should show datasource component for / router (using memory router)", () => {
//const component = mount(
//<MemoryRouter initialentries="{['/table/datasource']}">
//<Datasource />
//</MemoryRouter>
//);
//expect(component.find(Datasource)).toHaveLength(1);
//});
//});

//describe("routes using memory router", () => {
//it("should show Command Form component for / router (using memory router)", () => {
//const onSubmitFn = jest.fn();
//const component = mount(
//<MemoryRouter initialentries="{['/commands/:command']}">
//<CommandForm />
//</MemoryRouter>
//);
//const wrapper = mount(<Form onSubmit={onSubmitFn} />);
//const form = wrapper.find("form");
//form.simulate("submit");
//expect(onSubmitFn).toHaveBeenCalledTimes(1);
//expect(component.find(CommandForm)).toHaveBeenCalledTimes(1);
//});
//});
