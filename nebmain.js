<div class="row">
    <div id="sidebar-container" class="col-sm-3 dnp">
        <div ng-include="'views/batchsidebar-50735e0344.html'"></div>
    </div>
    <div class="col-sm-9 ">
        <div class="row content">
        <form>
            <div id="input" class="col-sm-12">
                <div class="row">
                    <!-- <div class="blue explain" ng-click="openmodal('tmchangenote', 'md')">Note: Recent changes to Tm calculations</div> -->
                    <div class="col-sm-8">
                        <span class="fieldlabel">Product Group</span><br>
                        <select ng-model="input.group" ng-options="gr for gr in input.groupKeys" ng-change="setProducts()">
                            <!-- <option ng-repeat="gr in input.groupKeys" value="{{gr}}">{{gr}}</option> -->
                        </select><br>
                        <span class="fieldlabel">Polymerase/Kit</span><br>
                        <select ng-model="input.product" ng-options="pr.id as pr.name for pr in input.products" ng-change="setCt()">
                            <!-- <option ng-repeat="pr in input.productKeys" value="{{pr}}">{{pr}}</option> -->
                        </select><br>
                    </div>
                </div>
                <div class="row">
                    <div class="col-sm-8">
                        <div class="row">
                            <div class="col-sm-7">
                                <span class="fieldlabel">Primer Concentration (nM)</span><br>
                                <input id="ct" ng-class="ctstatus" ng-model="input.ct" type="number" required ng-change="runCalc2()">
                            </div>
                            <div class="col-sm-5">
                                <div class="dnp refresh-holder">
                                    
                                    <a class="btn btn-link" ng-click="setCt()"><span class="glyphicon glyphicon-refresh"></span> Reset concentration </a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <br>
                <div class="row">
                    <div class="col-sm-12">
                        <span class="fieldlabel">Primer Pairs</span><br>
                        <div id="fileinputcontainer">
                            <span>Type/paste sequences below or load primer pairs from file: </span>
                            <input type="file" on-read-file="processFileData(filedata)" ng-model="input.filename" id="fileinput"/>
                            <!-- <input type="file" on-read-file="loadSeqFromFile($fileName, $fileContent)"/> -->
                        </div>
                        <div id="checkboxcontainer">
                            <input class="" type="checkbox" id="interleaved" value="{{true}}"  ng-model="input.interleaved" ng-change="runCalc3(input.interleaved)"/>
                            <label for="interleaved"><span class="">Interleaved data (one primer per line)</span></label>
                        </div>
                        <textarea id="batchinput" ng-model="input.batch"  ng-class="p1status" ng-blur="runCalc3(input.interleaved)" placeholder="ID#1 ; Primer1 ; ID#2 ; Primer2 -newline-">
                        </textarea>
                        
                    </div>
                </div>
                <div class="row">
                    <div class="col-sm-8">
                        <div class="row">
                            <div class="col-sm-7">
                                <a ng-click="switch2single()" class="btn btn-link dnp">Switch to single pair mode</a>
                            </div>
                            <div class="col-sm-5">
                                <a ng-click="clearCalc()" class="btn btn-link dnp" >Clear</a>
                                <br>
                                <a ng-click="prefill()" class="btn btn-link dnp">Use example input</a>
                                <br>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row">
                <div class="col-sm-12">
                    <div id="result" class="col-sm-12" ng-hide="output">
                        <span class="invalidseq">{{novaliddatamsg}}</span>
                    </div>
                </div>
            </div>

            <div class="row">
                <div class="col-sm-12">
                    <div id="result" ng-show="output.length">
                        <div ng-hidex="output.showresultstable"><h4>{{runmsg}}</h4></div>
                        <br>
                        <a ng-click="toggle_data_display()" class="btn btn-link dnp">{{data_toggle_label}} results</a>

                        <a class="downloadfile" href="" ng-click="downloadData()">
                            <img ng-src="images/download3i-72b9cb92ff.png">
                        </a>
                        <br><br>
                        <table class="batchresultstablex" ng-show="output.showresultstable">
                            <thead>
                                <tr>
                                    <th ng-repeat="el in ['ID','Sequence','Tm','Ta', 'Notes']">
                                        {{el}}
                                    </th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr ng-repeat="row in result.batch2">
                                    <td ng-repeat="idx in [0,1,2,3,4]" class="batchresultscell">{{row[idx]}}</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
            </div>
        </form>
        </div>
        <div class="row">
            <div class="col-sm-11">
                <hr>
                <div id="crit" class="notes">
                    <ul>
                        <li ng-repeat="item in result.critlist">{{item}}</li>
                    </ul>
                </div>
                <div id="warn" class="notes" ng-show="result.ta">
                    <ul>
                        <li ng-repeat="item in result.itemlist">{{item}}</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</div>
<script>
    gtag('event', 'screen_view', {
        'send_to': 'neb',
        'screen_name': 'Tm Calculator Batch Mode'
    });
</script>
