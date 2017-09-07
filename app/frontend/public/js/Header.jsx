import React, { Component } from 'react';

import Menu from './Menu';

export default class Header extends Component {
    render() {
        const HOME_MENU = ['Data Acquisition', 'Experiments', 'Information', 'About'];

        return(
            <div>
                <h1 className="main-title">noobelectric</h1>
                <div className="header">
                    <Menu
                        onClick={this.props.onClick}
                        labels={HOME_MENU}
                    />

                {/* <span className="glyphicon glyphicon-home home-btn"></span> */}
                </div>
            </div>
        )
    }
}
