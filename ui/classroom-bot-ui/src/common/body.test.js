import React, { Component } from "react";
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
//import Datasource from "../main/datasource";
import GroupForm from "../main/groupForm";
import CourseForm from "../main/courseForm";
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

describe("routes using memory router", () => {
  it("should show Command form component for / router (using memory router)", () => {
    const component = mount(
      <MemoryRouter initialentries="{['/form/course/abc12450145']}">
        render ={" "}
        {(props) => <CourseForm {...props} key={this.props.location.key} />}
      </MemoryRouter>
    );
    expect(component.find(CourseForm)).toHaveLength(1);
  });
});

describe("routes using memory router", () => {
  it("should show group form component for / router (using memory router)", () => {
    const component = mount(
      <MemoryRouter initialentries="{['/form/group']}">
        <GroupForm />
      </MemoryRouter>
    );
    expect(component.find(GroupForm)).toHaveLength(1);
  });
});

//describe("routes using memory router", () => {
//it("should show datasource component for / router (using memory router)", () => {
//const component = mount(
//<MemoryRouter initialentries="{['/table/group']}">
//<Datasource />
//</MemoryRouter>
//);
//expect(component.find(Datasource)).toHaveLength(1);
//});
//});
