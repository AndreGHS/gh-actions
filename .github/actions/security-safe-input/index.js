const core = require('@actions/core');

async function run() {
    try {
        const input = core.getInput('pr-title');
        if (prTitle.startsWith('feat')) {
            core.info('PR is a feature');
        }
        else {
            core.info('PR is not a featur');
        }
    }
    catch (error) {
        core.setFailed('Error: ' + error.message)
    }
}

run();