
"use strict";

let Load = require('./Load.js')
let IsProgramSaved = require('./IsProgramSaved.js')
let GetProgramState = require('./GetProgramState.js')
let RawRequest = require('./RawRequest.js')
let Popup = require('./Popup.js')
let IsProgramRunning = require('./IsProgramRunning.js')
let GetLoadedProgram = require('./GetLoadedProgram.js')
let AddToLog = require('./AddToLog.js')
let GetSafetyMode = require('./GetSafetyMode.js')
let GetRobotMode = require('./GetRobotMode.js')

module.exports = {
  Load: Load,
  IsProgramSaved: IsProgramSaved,
  GetProgramState: GetProgramState,
  RawRequest: RawRequest,
  Popup: Popup,
  IsProgramRunning: IsProgramRunning,
  GetLoadedProgram: GetLoadedProgram,
  AddToLog: AddToLog,
  GetSafetyMode: GetSafetyMode,
  GetRobotMode: GetRobotMode,
};
