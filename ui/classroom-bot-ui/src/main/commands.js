import React from 'react'
import Table from 'react-bootstrap/Table'

function Commands () {
    return (
        <div>
            <div class="container-fluid">
                <div class="row">
                    <div class="col-sm-12 table-div">
                        <Table striped bordered hover size="sm">
                            <thead>
                                <tr>
                                    <th>#</th>
                                    <th>Command</th>
                                    <th>Template</th>
                                    <th>Active</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>1</td>
                                    <td><a href="/commands/create">Create Link</a></td>
                                    <td>@Bot create link [document]</td>
                                    <td>True</td>
                                </tr>
                                <tr>
                                    <td>2</td>
                                    <td><a href="/commands/remove">Remove Link</a></td>
                                    <td>@Bot remove link [document]</td>
                                    <td>False</td>
                                </tr>
                                <tr>
                                    <td>3</td>
                                    <td><a href="/commands/get">Get Link</a></td>
                                    <td>@Bot get link [document]</td>
                                    <td>False</td>
                                </tr>
                            </tbody>
                        </Table>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Commands;