import React, { Component } from 'react'
import { Table } from 'react-bootstrap';

export class Home extends Component {

    constructor(props) {
        super(props);
        this.state = { emps: [], deps: [] }
    }

    refreshList() {
        fetch(process.env.REACT_APP_API + 'employee/')
            .then(response => response.json())
            .then(data => {
                this.setState({ emps: data });
            });
        fetch(process.env.REACT_APP_API + 'department/')
            .then(response => response.json())
            .then(data => {
                this.setState({ deps: data });
            });
    }

    componentDidMount() {
        this.refreshList();
    }

    render() {
        const { deps, emps } = this.state;
        return (
            <div>
                <div>
                    <h3>Departemnts</h3>
                    <Table className="mt-4" striped bordered hover size="sm">
                        <thead>
                            <tr>
                                <th>DepartmentId</th>
                                <th>DepartmentName</th>
                            </tr>
                        </thead>
                        <tbody>
                            {deps.map(dep =>
                                <tr key={dep.departmentId}>
                                    <td>{dep.departmentId}</td>
                                    <td>{dep.departmentName}</td>
                                </tr>)}
                        </tbody>

                    </Table>
                </div>
                <div>
                    <h3>Employees</h3>
                    <Table className="mt-4" striped bordered hover size="sm">
                        <thead>
                            <tr>
                                <th>EmployeeId</th>
                                <th>EmployeeName</th>
                                <th>Department</th>
                                <th>DOJ</th>
                            </tr>
                        </thead>
                        <tbody>
                            {emps.map(emp =>
                                <tr key={emp.employeeId}>
                                    <td>{emp.employeeId}</td>
                                    <td>{emp.employeeName}</td>
                                    <td>{emp.department}</td>
                                    <td>{emp.dateOfJoin}</td>

                                </tr>)}
                        </tbody>

                    </Table>
                </div>

            </div>
        )
    }
}