// Current section Action
export const currentSectionAction = (section) => {
    //console.log('=====> currentSectionAction: triggered');
    return {
        type: 'CURRENT_SECTION',
        payload: {
            section: section
        }
    }
}