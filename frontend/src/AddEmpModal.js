import React, { Component } from 'react';
import { Modal, Button, Row, Col, Form, Image } from 'react-bootstrap';

export class AddEmpModal extends Component {
    constructor(props) {
        super(props);
        this.state = { deps: [], image: "http://127.0.0.1:8000/media/uploads/anonymous.png" };
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleimage = this.handleimage.bind(this)
    }

    componentDidMount() {

        fetch(process.env.REACT_APP_API + 'department')
            .then(response => response.json())
            .then(data => {
                this.setState({ deps: data });
            });
    }
    updateimage() {
        this.setState({ image: "http://127.0.0.1:8000/media/uploads/anonymous.png" })
    }

    handleSubmit(event) {
        event.preventDefault();
        event.preventDefault();
        const formData = new FormData();
        formData.append("employeeId", null)
        formData.append("employeeName", event.target.EmployeeName.value)
        formData.append("department", event.target.Department.value)
        formData.append("dateOfJoin", event.target.DateOfJoining.value)
        if (this.state.image !== "http://127.0.0.1:8000/media/uploads/anonymous.png") { formData.append("photo", this.state.image) }
        fetch(process.env.REACT_APP_API + 'employee/', {
            method: 'POST',
            body: formData
        })
            .then(res => res.json())
            .then((result) => {
                alert(result);
            },
                (error) => {
                    alert('Failed');
                })
    }

    handleimage(event) {
        var file = event.target.files[0];
        var reader = new FileReader();
        var url = reader.readAsDataURL(file);

        reader.onloadend = function (e) {
            this.setState({
                image: [reader.result]
            })
        }.bind(this);
        console.log(url)
    }

    render() {
        return (
            <div className="container">

                <Modal
                    {...this.props}
                    size="lg"
                    aria-labelledby="contained-modal-title-vcenter"
                    centered
                >
                    <Modal.Header>
                        <Modal.Title id="contained-modal-title-vcenter">
                            Add Employee
                        </Modal.Title>
                    </Modal.Header>
                    <Modal.Body>

                        <Row>
                            <Col sm={6}>
                                <Form onSubmit={this.handleSubmit}>
                                    <Form.Group controlId="EmployeeName">
                                        <Form.Label>EmployeeName</Form.Label>
                                        <Form.Control type="text" name="EmployeeName" required
                                            placeholder="EmployeeName" />
                                    </Form.Group>

                                    <Form.Group controlId="Department">
                                        <Form.Label>Department</Form.Label>
                                        <Form.Control as="select">
                                            {this.state.deps.map(dep =>
                                                <option key={dep.departmentId}>{dep.departmentName}</option>)}
                                        </Form.Control>
                                    </Form.Group>

                                    <Form.Group controlId="DateOfJoining">
                                        <Form.Label>DateOfJoining</Form.Label>
                                        <Form.Control
                                            type="date"
                                            name="DateOfJoining"
                                            required
                                            placeholder="DateOfJoining"
                                        />


                                    </Form.Group>

                                    <Form.Group>
                                        <Button variant="primary" type="submit">
                                            Add Employee
                                        </Button>
                                    </Form.Group>
                                </Form>
                            </Col>

                            <Col sm={6}>
                                <Image width="200px" height="200px" src={this.state.image} />
                                <input onChange={this.handleimage} name="image" type="File" />
                            </Col>
                        </Row>
                    </Modal.Body>

                    <Modal.Footer>
                        <Button variant="danger" onClick={() => { this.props.onHide(); this.updateimage() }}>Close</Button>
                    </Modal.Footer>

                </Modal>

            </div>
        )
    }

}